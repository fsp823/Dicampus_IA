# libro.py

class Libro:
    def __init__(self, titulo, autor, precio, cantidad=1):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.cantidad = cantidad
        self.prestado = False

    def __str__(self):
        estado = "PRESTADO" if self.prestado else "DISPONIBLE"
        return f"[{estado}] '{self.titulo}' de {self.autor} — ${self.precio:.2f} ({self.cantidad} unid.)"