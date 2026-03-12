# menu.py

from tareas.tareas import (
    agregar_tarea,
    completar_tarea,
    eliminar_tarea,
    listar_tareas,
)


def menu():

    # Datos de prueba (igual que el original)
    agregar_tarea("Comprar leche")
    agregar_tarea("Estudiar Python")
    agregar_tarea("Hacer ejercicio")

    while True:
        print("\n╔══════════════════════════╗")
        print("║       TODO  LIST         ║")
        print("╠══════════════════════════╣")
        print("║ 1. Añadir tarea          ║")
        print("║ 2. Completar tarea       ║")
        print("║ 3. Eliminar tarea        ║")
        print("║ 4. Ver tareas            ║")
        print("║ 0. Salir                 ║")
        print("╚══════════════════════════╝")

        op = input("  Opción: ").strip()

        if op == "0":
            print("  👋 ¡Hasta luego!")
            break

        elif op == "1":
            desc = input("  Descripción: ")
            _, msg = agregar_tarea(desc)
            print(f"  {msg}")

        elif op == "2":
            id_str = input("  ID de la tarea: ")
            _, msg = completar_tarea(id_str)
            print(f"  {msg}")

        elif op == "3":
            id_str = input("  ID a eliminar: ")
            _, msg = eliminar_tarea(id_str)
            print(f"  {msg}")

        elif op == "4":
            listar_tareas()

        else:
            print("  ⚠️  Opción no válida.")