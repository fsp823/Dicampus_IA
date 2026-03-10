# ============================================================
# PASO 1 — TODO EN UN SOLO ARCHIVO (sin modularizar)
# ============================================================
# ⚠️ Problema: difícil de mantener, escalar o reusar código.
# Todo: clases, lógica y menú viven juntos en un caos.
# ============================================================

class Libro:
    def __init__(self, titulo, autor, precio, cantidad=1):
        self.titulo    = titulo
        self.autor     = autor
        self.precio    = precio
        self.cantidad  = cantidad
        self.prestado  = False

    def __str__(self):
        estado = "PRESTADO" if self.prestado else "DISPONIBLE"
        return f"[{estado}] '{self.titulo}' de {self.autor} — ${self.precio:.2f} ({self.cantidad} unid.)"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre  = nombre
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
            print("⚠️  El libro ya está prestado.")
        else:
            libro.prestado = True
            print(f"📖 Libro '{titulo}' prestado con éxito.")

    def devolver_libro(self, titulo: str):
        libro = self.buscar_libro(titulo)
        if not libro:
            print("❌ Libro no encontrado.")
        elif not libro.prestado:
            print("⚠️  El libro no estaba prestado.")
        else:
            libro.prestado = False
            print(f"🔄 Libro '{titulo}' devuelto. ¡Gracias!")

    def comprar_libro(self, titulo: str, autor: str, precio: float, cantidad: int = 1):
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
            print("⚠️  Sin stock disponible.")
        elif libro.prestado:
            print("⚠️  El libro está prestado, no se puede vender.")
        else:
            libro.cantidad -= 1
            self.ingresos += libro.precio
            print(f"💰 Vendido '{libro.titulo}' por ${libro.precio:.2f}. Ingresos totales: ${self.ingresos:.2f}")

    def mostrar_catalogo(self):
        print(f"\n📚 Catálogo de '{self.nombre}':")
        if not self.catalogo:
            print("   (vacío)")
        for libro in self.catalogo:
            print(f"   {libro}")


# ── Menú ──────────────────────────────────────────────────
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