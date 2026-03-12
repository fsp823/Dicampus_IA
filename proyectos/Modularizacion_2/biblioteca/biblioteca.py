# biblioteca.py

from libro import Libro


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo: list[Libro] = []
        self.ingresos = 0.0

    def agregar_libro(self, libro: Libro):
        self.catalogo.append(libro)
        print(f"✅ '{libro.titulo}' añadido al catálogo.")

    def buscar_libro(self, titulo: str) -> Libro | None:
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo: str):
        libro = self.buscar_libro(titulo)

        if not libro:
            print("❌ Libro no encontrado.")
        elif libro.prestado:
            print("⚠️ El libro ya está prestado.")
        else:
            libro.prestado = True
            print(f"📖 Libro '{titulo}' prestado con éxito.")

    def devolver_libro(self, titulo: str):
        libro = self.buscar_libro(titulo)

        if not libro:
            print("❌ Libro no encontrado.")
        elif not libro.prestado:
            print("⚠️ El libro no estaba prestado.")
        else:
            libro.prestado = False
            print(f"🔄 Libro '{titulo}' devuelto. ¡Gracias!")

    def comprar_libro(self, titulo, autor, precio, cantidad=1):
        existente = self.buscar_libro(titulo)

        if existente:
            existente.cantidad += cantidad
            print(f"📦 Stock de '{titulo}' actualizado a {existente.cantidad} unidades.")
        else:
            nuevo = Libro(titulo, autor, precio, cantidad)
            self.agregar_libro(nuevo)

    def vender_libro(self, titulo: str):
        libro = self.buscar_libro(titulo)

        if not libro:
            print("❌ Libro no encontrado.")
        elif libro.cantidad <= 0:
            print("⚠️ Sin stock disponible.")
        elif libro.prestado:
            print("⚠️ El libro está prestado, no se puede vender.")
        else:
            libro.cantidad -= 1
            self.ingresos += libro.precio
            print(
                f"💰 Vendido '{libro.titulo}' por ${libro.precio:.2f}. "
                f"Ingresos totales: ${self.ingresos:.2f}"
            )

    def mostrar_catalogo(self):
        print(f"\n📚 Catálogo de '{self.nombre}':")

        if not self.catalogo:
            print("   (vacío)")
            return

        for libro in self.catalogo:
            print(f"   {libro}")