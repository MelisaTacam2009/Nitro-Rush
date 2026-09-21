# ==========================================
#              NITRO RUSH
# ==========================================

print("======================================")
print("              NITRO RUSH")
print("======================================")
print("¡Bienvenido a NITRO RUSH!")
print("Prepárate para competir y demostrar")
print("tus habilidades como corredor.")
print("¡Que comience la carrera!")
print("======================================")


# ==========================================
#                 MENÚ
# ==========================================

opcion = 0

while opcion != 6:

    print("\n========== MENÚ NITRO RUSH ==========")
    print("1. CLUB")
    print("2. CARRETERA")
    print("3. BOSQUE")
    print("4. MONTAÑA")
    print("5. FINAL")
    print("6. SALIR")
    print("=====================================")

    opcion = int(input("Selecciona una opción: "))

    # OPCIÓN 1
    if opcion == 1:
        print("\n=====================================")
        print("          NIVEL CLUB")
        print("=====================================")
        print("Has entrado al nivel CLUB.")
        print("Prepárate para comenzar la carrera.")
        input("\nPresiona ENTER para regresar al menú...")

    # OPCIÓN 2
    elif opcion == 2:
        print("\n=====================================")
        print("        NIVEL CARRETERA")
        print("=====================================")
        print("Has entrado al nivel CARRETERA.")
        print("¡Acelera y evita los obstáculos!")
        input("\nPresiona ENTER para regresar al menú...")

    # OPCIÓN 3
    elif opcion == 3:
        print("\n=====================================")
        print("          NIVEL BOSQUE")
        print("=====================================")
        print("Has entrado al nivel BOSQUE.")
        print("¡Ten cuidado con el camino!")
        input("\nPresiona ENTER para regresar al menú...")

    # OPCIÓN 4
    elif opcion == 4:
        print("\n=====================================")
        print("         NIVEL MONTAÑA")
        print("=====================================")
        print("Has entrado al nivel MONTAÑA.")
        print("¡Supera las curvas y los obstáculos!")
        input("\nPresiona ENTER para regresar al menú...")

    # OPCIÓN 5
    elif opcion == 5:
        print("\n=====================================")
        print("            NIVEL FINAL")
        print("=====================================")
        print("¡Has llegado a la carrera final!")
        print("Demuestra todo lo que has aprendido.")
        input("\nPresiona ENTER para regresar al menú...")

    # OPCIÓN 6
    elif opcion == 6:
        print("\n=====================================")
        print("     ¡GRACIAS POR JUGAR!")
        print("          NITRO RUSH")
        print("=====================================")

    # OPCIÓN INCORRECTA
    else:
        print("\nOpción no válida.")
        print("Selecciona un número del 1 al 6.")
