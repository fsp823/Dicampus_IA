# main.py

from biblioteca import Biblioteca
from libro import Libro


def menu():
    inventario = Biblioteca("Biblioteca Central")

    # Datos de prueba
    inventario.agregar_libro(Libro("El Quijote", "Cervantes", 15.00, 3))
    inventario.agregar_libro(Libro("Cien años", "García Márquez", 12.50, 2))
    inventario.agregar_libro(Libro("1984", "Orwell", 10.00, 1))

    opciones = {
        "1": lambda: inventario.prestar_libro(input("Título: ")),
        "2": lambda: inventario.devolver_libro(input("Título: ")),
        "3": lambda: inventario.comprar_libro(
            input("Título: "),
            input("Autor: "),
            float(input("Precio: ")),
            int(input("Cantidad: "))
        ),
        "4": lambda: inventario.vender_libro(input("Título: ")),
        "5": inventario.mostrar_catalogo,
    }

    while True:
        print("""
=== MENÚ ===
1. Prestar
2. Devolver
3. Comprar
4. Vender
5. Catálogo
0. Salir
""")

        op = input("Opción: ").strip()

        if op == "0":
            print("👋 ¡Hasta luego!")
            break
        elif op in opciones:
            opciones[op]()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()