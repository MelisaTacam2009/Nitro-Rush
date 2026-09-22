# ==========================================
#              NITRO RUSH
#        Proyecto - Programador Junior
# ==========================================

import random


class Carro:
    def __init__(self, nombre, velocidad, nitro):
        self.nombre = nombre
        self.velocidad = velocidad
        self.nitro = nitro

    def mostrar(self):
        print(f"{self.nombre} | Velocidad: {self.velocidad} | Nitro: {self.nitro}")


class Rival:
    def __init__(self, nombre, velocidad_min, velocidad_max):
        self.nombre = nombre
        self.velocidad_min = velocidad_min
        self.velocidad_max = velocidad_max

    def correr(self):
        return random.randint(self.velocidad_min, self.velocidad_max)


class Nivel:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad


class NitroRush:
    def __init__(self):
        self.puntos = 0
        self.vidas = 3
        self.nivel_actual = 0
        self.carro = None

        self.carros = [
            Carro("Rayo", 8, 3),
            Carro("Furia", 7, 4),
            Carro("Tormenta", 9, 2)
        ]

        self.rivales = [
            Rival("Max", 6, 9),
            Rival("Shadow", 7, 10),
            Rival("Blaze", 5, 10)
        ]

        self.niveles = [
            Nivel("CLUB", 1),
            Nivel("CARRETERA", 2),
            Nivel("BOSQUE", 3),
            Nivel("MONTAÑA", 4),
            Nivel("FINAL", 5)
        ]

    def bienvenida(self):
        print("\n======================================")
        print("              NITRO RUSH")
        print("======================================")
        print("¡Bienvenido a NITRO RUSH!")
        print("Prepárate para competir y demostrar")
        print("tus habilidades como corredor.")
        print("¡Que comience la carrera!")
        print("======================================")

    def instrucciones(self):
        print("\n========== INSTRUCCIONES ==========")
        print("1. Selecciona un carro antes de comenzar.")
        print("2. Cada carrera tiene 5 turnos.")
        print("3. Puedes acelerar, frenar, esquivar o usar nitro.")
        print("4. El nitro aumenta tu velocidad, pero es limitado.")
        print("5. Los obstáculos pueden hacerte perder puntos.")
        print("6. Si ganas, avanzas al siguiente nivel.")
        print("7. Si pierdes, pierdes una vida y puedes reintentar.")
        print("8. Si pierdes tus 3 vidas, termina el juego.")
        print("9. Gana los 5 niveles para ser el campeón.")
        print("===================================")
        input("\nPresiona ENTER para regresar al menú...")

    def seleccionar_carro(self):
        print("\n========== SELECCIONA TU CARRO ==========")

        for i, carro in enumerate(self.carros, 1):
            print(f"{i}. ", end="")
            carro.mostrar()

        while True:
            try:
                opcion = int(input("Selecciona un carro (1-3): "))
                if 1 <= opcion <= 3:
                    self.carro = self.carros[opcion - 1]
                    print(f"\nElegiste: {self.carro.nombre}")
                    return
                print("Selecciona un número del 1 al 3.")
            except ValueError:
                print("Debes escribir un número.")

    def correr_carrera(self, nivel):
        print(f"\n========== NIVEL {nivel.nombre} ==========")
        print("¡La carrera está por comenzar!")
        print(f"Dificultad: {nivel.dificultad}/5")
        print("Rivales: Max, Shadow y Blaze")

        distancia_jugador = 0
        nitro_disponible = self.carro.nitro

        for turno in range(1, 6):
            print(f"\n--- TURNO {turno}/5 ---")
            print(f"Puntos: {self.puntos}")
            print(f"Vidas: {self.vidas}")
            print(f"Nitro disponible: {nitro_disponible}")
            print("1. Acelerar")
            print("2. Frenar")
            print("3. Esquivar")
            print("4. Usar Nitro")

            while True:
                try:
                    accion = int(input("Elige una acción: "))
                    if 1 <= accion <= 4:
                        break
                    print("Elige una opción del 1 al 4.")
                except ValueError:
                    print("Debes escribir un número.")

            obstaculo = random.randint(1, 5 + nivel.dificultad)

            if accion == 1:
                avance = self.carro.velocidad + random.randint(1, 4)
                print("¡Aceleraste!")
                if obstaculo >= 5:
                    avance -= 2
                    print("¡Encontraste un obstáculo!")
                distancia_jugador += max(avance, 0)
                self.puntos += 10

            elif accion == 2:
                avance = max(self.carro.velocidad - 3, 1)
                distancia_jugador += avance
                self.puntos += 5
                print("Frenaste para controlar mejor el carro.")

            elif accion == 3:
                avance = self.carro.velocidad + random.randint(0, 2)
                if obstaculo >= 4:
                    print("¡Esquivaste el obstáculo!")
                    self.puntos += 20
                else:
                    print("No había un obstáculo importante.")
                    self.puntos += 10
                distancia_jugador += avance

            else:
                if nitro_disponible > 0:
                    avance = self.carro.velocidad + 8
                    distancia_jugador += avance
                    nitro_disponible -= 1
                    self.puntos += 25
                    print("¡¡NITRO ACTIVADO!! ¡Aceleración máxima!")
                else:
                    print("Ya no tienes nitro. Debes elegir otra estrategia.")

        print("\n========== RESULTADO ==========")
        print(f"Distancia del jugador: {distancia_jugador}")

        resultados = [(distancia_jugador, "Tú")]
        for rival in self.rivales:
            # La dificultad aumenta la competencia de los rivales.
            ajuste = nivel.dificultad
            distancia_rival = rival.correr() + rival.correr() + ajuste
            resultados.append((distancia_rival, rival.nombre))

        resultados.sort(reverse=True)

        print("\nPosiciones:")
        for posicion, (distancia, nombre) in enumerate(resultados, 1):
            print(f"{posicion}. {nombre} - {distancia} puntos de carrera")

        if resultados[0][1] == "Tú":
            print("\n🏆 ¡GANASTE LA CARRERA!")
            self.puntos += 100
            return True

        print(f"\n😔 {resultados[0][1]} ganó la carrera.")
        self.vidas -= 1
        print(f"Perdiste una vida. Vidas restantes: {self.vidas}")
        return False

    def jugar(self):
        self.puntos = 0
        self.vidas = 3
        self.nivel_actual = 0

        self.seleccionar_carro()

        while self.nivel_actual < len(self.niveles):
            nivel = self.niveles[self.nivel_actual]
            gano = self.correr_carrera(nivel)

            if gano:
                self.nivel_actual += 1

                if self.nivel_actual < len(self.niveles):
                    print(f"\n¡Excelente! Desbloqueaste el nivel {self.niveles[self.nivel_actual].nombre}.")
                    input("Presiona ENTER para continuar...")
            else:
                if self.vidas > 0:
                    print("\nPuedes intentar nuevamente este nivel.")
                    input("Presiona ENTER para reintentar...")
                else:
                    print("\n===================================")
                    print("             GAME OVER")
                    print("===================================")
                    print(f"Puntuación final: {self.puntos}")
                    input("Presiona ENTER para regresar al menú...")
                    return

        print("\n===================================")
        print("       🏆 ¡ERES EL CAMPEÓN! 🏆")
        print("          NITRO RUSH")
        print("===================================")
        print(f"Puntuación final: {self.puntos}")
        print("¡Completaste los 5 niveles!")
        input("\nPresiona ENTER para regresar al menú...")

    def menu(self):
        opcion = 0

        while opcion != 3:
            print("\n========== MENÚ NITRO RUSH ==========")
            print("1. JUGAR")
            print("2. INSTRUCCIONES")
            print("3. SALIR")
            print("=====================================")

            try:
                opcion = int(input("Selecciona una opción: "))
            except ValueError:
                print("\nOpción no válida. Escribe un número.")
                continue

            if opcion == 1:
                self.jugar()
            elif opcion == 2:
                self.instrucciones()
            elif opcion == 3:
                print("\n=====================================")
                print("     ¡GRACIAS POR JUGAR!")
                print("          NITRO RUSH")
                print("=====================================")
            else:
                print("\nOpción no válida. Selecciona 1, 2 o 3.")


# Programa principal
juego = NitroRush()
juego.bienvenida()
juego.menu()