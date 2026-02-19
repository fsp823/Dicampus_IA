from datetime import datetime
from typing import List, Optional


class Libro:
    def __init__(self, id: int, titulo: str, autor: str, isbn: str):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __repr__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{estado}]"


class Usuario:
    def __init__(self, id: int, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"{self.id} - {self.nombre} ({self.email})"


class Prestamo:
    def __init__(self, libro: Libro, usuario: Usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion: Optional[datetime] = None

    def devolver(self):
        self.fecha_devolucion = datetime.now()
        self.libro.disponible = True

    @property
    def activo(self) -> bool:
        return self.fecha_devolucion is None

    def __repr__(self):
        estado = "Activo" if self.activo else "Devuelto"
        return (
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} | "
            f"Fecha préstamo: {self.fecha_prestamo.strftime('%Y-%m-%d %H:%M')} | "
            f"Estado: {estado}"
        )


class Biblioteca:
    def __init__(self):
        self.libros: List[Libro] = []
        self.usuarios: List[Usuario] = []
        self.prestamos: List[Prestamo] = []

    # -------------------------
    # Gestión de libros
    # -------------------------

    def agregar_libro(self, libro: Libro):
        if any(l.isbn == libro.isbn for l in self.libros):
            raise ValueError("Ya existe un libro con ese ISBN")
        self.libros.append(libro)

    def buscar_libro_por_isbn(self, isbn: str) -> Optional[Libro]:
        return next((l for l in self.libros if l.isbn == isbn), None)

    # -------------------------
    # Gestión de usuarios
    # -------------------------

    def agregar_usuario(self, usuario: Usuario):
        if any(u.email == usuario.email for u in self.usuarios):
            raise ValueError("Ya existe un usuario con ese email")
        self.usuarios.append(usuario)

    def buscar_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        return next((u for u in self.usuarios if u.id == usuario_id), None)

    # -------------------------
    # Gestión de préstamos
    # -------------------------

    def prestar_libro(self, isbn: str, usuario_id: int) -> Prestamo:
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            raise ValueError("Libro no encontrado")

        if not libro.disponible:
            raise ValueError("Libro no disponible")

        usuario = self.buscar_usuario_por_id(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")

        libro.disponible = False
        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)
        return prestamo

    def devolver_libro(self, isbn: str):
        prestamo = next(
            (p for p in self.prestamos if p.libro.isbn == isbn and p.activo),
            None
        )
        if not prestamo:
            raise ValueError("No existe préstamo activo para ese libro")

        prestamo.devolver()
        return prestamo

    def prestamos_activos(self) -> List[Prestamo]:
        return [p for p in self.prestamos if p.activo]


# ======================================================
# MENÚ DE CONSOLA
# ======================================================

def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Registrar usuario")
    print("4. Listar usuarios")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Ver préstamos activos")
    print("0. Salir")


def main():
    biblioteca = Biblioteca()
    contador_libros = 1
    contador_usuarios = 1

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                isbn = input("ISBN: ")
                libro = Libro(contador_libros, titulo, autor, isbn)
                biblioteca.agregar_libro(libro)
                contador_libros += 1
                print("Libro agregado correctamente.")

            elif opcion == "2":
                print("\n--- Lista de libros ---")
                for libro in biblioteca.libros:
                    print(libro)

            elif opcion == "3":
                nombre = input("Nombre: ")
                email = input("Email: ")
                usuario = Usuario(contador_usuarios, nombre, email)
                biblioteca.agregar_usuario(usuario)
                contador_usuarios += 1
                print("Usuario registrado correctamente.")

            elif opcion == "4":
                print("\n--- Lista de usuarios ---")
                for usuario in biblioteca.usuarios:
                    print(usuario)

            elif opcion == "5":
                isbn = input("ISBN del libro: ")
                usuario_id = int(input("ID del usuario: "))
                biblioteca.prestar_libro(isbn, usuario_id)
                print("Préstamo registrado correctamente.")

            elif opcion == "6":
                isbn = input("ISBN del libro a devolver: ")
                biblioteca.devolver_libro(isbn)
                print("Libro devuelto correctamente.")

            elif opcion == "7":
                print("\n--- Préstamos activos ---")
                for prestamo in biblioteca.prestamos_activos():
                    print(prestamo)

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")

        except ValueError as e:
            print(f"Error: {e}")
            
            try:
                usuario_id = int(input("ID del usuario: "))
            except ValueError:
                print("ID debe ser un número entero")
            continue



if __name__ == "__main__":
    main()
