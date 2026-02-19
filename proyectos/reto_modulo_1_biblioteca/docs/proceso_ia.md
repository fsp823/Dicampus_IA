# Proceso de uso de IA en el desarrollo

## 1. Definición del problema
Se solicitó un sistema básico de gestión de biblioteca con:
- Gestión de libros
- Gestión de usuarios
- Gestión de préstamos y devoluciones

## 2. Diseño asistido por IA
La IA ayudó a:
- Definir entidades principales (Libro, Usuario, Prestamo, Biblioteca)
- Diseñar relaciones entre objetos
- Proponer validaciones de negocio
- Generar estructura de proyecto profesional

## 3. Generación de código
Se utilizó IA para:
- Crear clases orientadas a objetos
- Implementar validaciones básicas
- Generar pruebas unitarias con pytest
- Proponer documentación técnica

## 4. Validación
Se ejecutaron pruebas unitarias para verificar:
- Creación de libros
- Registro de préstamos
- Devoluciones correctas
- Manejo de errores

## 5. Mejora futura
- Persistencia en base de datos
- API REST (FastAPI)
- Autenticación
- Sistema de multas
- Recomendador basado en IA


Fase 1 – Planificación con IA

Prompt emitido por el usuario:

Genera 5 historias de usuario para un sistema de biblioteca, y genera también un diagrama de flujo (en texto) del proceso de préstamo.

Respuesta de Chat-GPT:

Perfecto. Aquí tienes 5 historias de usuario y un diagrama de flujo del proceso de préstamo en texto.

📚 Historias de Usuario – Sistema de Biblioteca
1️⃣ Registrar libro

Como bibliotecario
Quiero registrar un nuevo libro en el sistema
Para que pueda estar disponible para préstamos

Criterios de aceptación:

Se deben ingresar: título, autor, ISBN.

No se permite registrar libros con ISBN duplicado.

El libro queda marcado como "disponible" por defecto.

2️⃣ Registrar usuario

Como bibliotecario
Quiero registrar un nuevo usuario
Para que pueda solicitar préstamos

Criterios de aceptación:

Se deben ingresar: nombre y email.

No se permiten emails duplicados.

El usuario queda activo automáticamente.

3️⃣ Prestar libro

Como bibliotecario
Quiero registrar el préstamo de un libro a un usuario
Para llevar control de los libros prestados

Criterios de aceptación:

El libro debe existir en el sistema.

El libro debe estar disponible.

El usuario debe existir.

El sistema registra fecha de préstamo.

El libro cambia su estado a "no disponible".

4️⃣ Registrar devolución

Como bibliotecario
Quiero registrar la devolución de un libro
Para actualizar su disponibilidad

Criterios de aceptación:

Debe existir un préstamo activo del libro.

Se registra fecha de devolución.

El libro cambia a "disponible".

El préstamo deja de estar activo.

5️⃣ Consultar préstamos activos

Como bibliotecario
Quiero ver la lista de préstamos activos
Para identificar libros actualmente prestados

Criterios de aceptación:

Se muestran solo préstamos sin devolución registrada.

Se visualiza: libro, usuario, fecha de préstamo.

Puede filtrarse por usuario.

🔄 Diagrama de Flujo – Proceso de Préstamo (Texto)

[Inicio]
   |
   v
¿Libro existe?
   |---- No ----> [Mostrar error: Libro no encontrado] --> [Fin]
   |
  Sí
   |
   v
¿Libro disponible?
   |---- No ----> [Mostrar error: Libro no disponible] --> [Fin]
   |
  Sí
   |
   v
¿Usuario existe?
   |---- No ----> [Mostrar error: Usuario no encontrado] --> [Fin]
   |
  Sí
   |
   v
[Registrar préstamo]
   |
   v
[Guardar fecha de préstamo]
   |
   v
[Cambiar estado del libro a "No disponible"]
   |
   v
[Confirmar préstamo exitoso]
   |
   v
[Fin]

Fase 2 – Desarrollo con IA

Chat-GPT generó en primera instancia:

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
        return f"<Libro {self.titulo} - Disponible: {self.disponible}>"


class Usuario:
    def __init__(self, id: int, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"<Usuario {self.nombre}>"


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

    # -------------------------
    # Gestión de préstamos
    # -------------------------

    def prestar_libro(self, isbn: str, usuario_id: int) -> Prestamo:
        libro = self.buscar_libro_por_isbn(isbn)
        if not libro:
            raise ValueError("Libro no encontrado")

        if not libro.disponible:
            raise ValueError("Libro no disponible")

        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
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



El usuario escribió este prompt:

Genérame en biblioteca.py un menú de consola para acceder a las funciones e introducir los datos.

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


if __name__ == "__main__":
    main()


Fase 3 – Tests y automatización

El usuario escribió el prompt: Ahora genérame 5 test unitarios en un archivo llamado test_biblioteca.py

Chat-GPT respondió: 
Perfecto. Aquí tienes 5 test unitarios para el sistema, listos para usar con pytest.

Guárdalos en:

tests/test_biblioteca.py

📄 tests/test_biblioteca.py
import pytest
from src.biblioteca import Biblioteca, Libro, Usuario


def crear_biblioteca_base():
    biblioteca = Biblioteca()
    libro = Libro(1, "Clean Code", "Robert C. Martin", "12345")
    usuario = Usuario(1, "Ana López", "ana@email.com")
    biblioteca.agregar_libro(libro)
    biblioteca.agregar_usuario(usuario)
    return biblioteca


# 1️⃣ Test: Agregar libro correctamente
def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro(1, "Python 101", "Autor X", "111")
    biblioteca.agregar_libro(libro)

    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0].titulo == "Python 101"


# 2️⃣ Test: No permitir ISBN duplicado
def test_no_permitir_isbn_duplicado():
    biblioteca = Biblioteca()
    libro1 = Libro(1, "Libro A", "Autor", "999")
    libro2 = Libro(2, "Libro B", "Autor", "999")

    biblioteca.agregar_libro(libro1)

    with pytest.raises(ValueError):
        biblioteca.agregar_libro(libro2)


# 3️⃣ Test: Prestar libro correctamente
def test_prestar_libro_correctamente():
    biblioteca = crear_biblioteca_base()
    prestamo = biblioteca.prestar_libro("12345", 1)

    assert prestamo.libro.disponible is False
    assert len(biblioteca.prestamos_activos()) == 1


# 4️⃣ Test: No prestar libro no disponible
def test_no_prestar_libro_no_disponible():
    biblioteca = crear_biblioteca_base()
    biblioteca.prestar_libro("12345", 1)

    with pytest.raises(ValueError):
        biblioteca.prestar_libro("12345", 1)


# 5️⃣ Test: Devolver libro correctamente
def test_devolver_libro():
    biblioteca = crear_biblioteca_base()
    biblioteca.prestar_libro("12345", 1)
    biblioteca.devolver_libro("12345")

    assert len(biblioteca.prestamos_activos()) == 0
    libro = biblioteca.buscar_libro_por_isbn("12345")
    assert libro.disponible is True

▶️ Ejecutar los tests

Desde la raíz del proyecto:

pytest

El usuario escribió: Hazme pruebas unitarias incluyendo el menú de consola

Chat-GPT respondió: 

Perfecto. Aquí tienes un archivo test_biblioteca.py con pruebas unitarias que incluyen el menú de consola, usando pytest, monkeypatch y capsys para simular input() y capturar la salida por pantalla.

Guárdalo en:

tests/test_biblioteca.py


📄 tests/test_biblioteca.py
import pytest
from src import biblioteca


# ======================================================
# TESTS DE LÓGICA DE NEGOCIO
# ======================================================

def crear_biblioteca_base():
    b = biblioteca.Biblioteca()
    libro = biblioteca.Libro(1, "Clean Code", "Robert C. Martin", "12345")
    usuario = biblioteca.Usuario(1, "Ana López", "ana@email.com")
    b.agregar_libro(libro)
    b.agregar_usuario(usuario)
    return b


def test_agregar_libro():
    b = biblioteca.Biblioteca()
    libro = biblioteca.Libro(1, "Python 101", "Autor X", "111")
    b.agregar_libro(libro)

    assert len(b.libros) == 1
    assert b.libros[0].titulo == "Python 101"


def test_prestar_y_devolver_libro():
    b = crear_biblioteca_base()

    prestamo = b.prestar_libro("12345", 1)
    assert prestamo.libro.disponible is False
    assert len(b.prestamos_activos()) == 1

    b.devolver_libro("12345")
    assert len(b.prestamos_activos()) == 0
    assert b.buscar_libro_por_isbn("12345").disponible is True


# ======================================================
# TESTS DEL MENÚ DE CONSOLA
# ======================================================

def test_menu_agregar_libro(monkeypatch, capsys):
    """
    Simula:
    1 -> Agregar libro
    datos del libro
    0 -> Salir
    """
    inputs = iter([
        "1",            # opción agregar libro
        "Libro Test",   # título
        "Autor Test",   # autor
        "999",          # isbn
        "0"             # salir
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    biblioteca.main()

    captured = capsys.readouterr()
    assert "Libro agregado correctamente." in captured.out


def test_menu_prestar_libro(monkeypatch, capsys):
    """
    Flujo simulado:
    1 -> Agregar libro
    3 -> Registrar usuario
    5 -> Prestar libro
    0 -> Salir
    """
    inputs = iter([
        "1",            # agregar libro
        "Libro Test",
        "Autor Test",
        "555",

        "3",            # registrar usuario
        "Juan",
        "juan@email.com",

        "5",            # prestar libro
        "555",          # isbn
        "1",            # id usuario

        "0"             # salir
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    biblioteca.main()

    captured = capsys.readouterr()
    assert "Préstamo registrado correctamente." in captured.out


def test_menu_opcion_invalida(monkeypatch, capsys):
    """
    Simula una opción inválida
    """
    inputs = iter([
        "99",   # opción inválida
        "0"     # salir
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    biblioteca.main()

    captured = capsys.readouterr()
    assert "Opción no válida." in captured.out

🧪 Qué estamos probando

Incluye:

✔ Lógica de negocio

Agregar libro

Prestar y devolver libro

✔ Menú de consola

Flujo completo de agregar libro

Flujo completo de préstamo

Manejo de opción inválida

Simulación real de interacción con usuario

▶ Ejecutar

pytest -v


Automatización “normal” (scripts, GitHub Actions)

-Pruebas automáticas

-Ejecutar pytest en cada commit o pull request.

-Reportar resultados y cobertura de código.

GitHub Actions puede correr los tests en Linux, Windows y macOS.


CI/CD básico

-Construir paquetes o contenedores Docker automáticamente.

-Desplegar una versión demo en un servidor o entorno de staging.

-Actualización de dependencias

-Ejecutar scripts para verificar que requirements.txt esté actualizado.

-Alertas automáticas si alguna librería tiene vulnerabilidades.

-Generación de reportes simples

-Crear reportes de pruebas unitarias, cobertura o métricas de código.

-Guardar resultados como artefactos en GitHub Actions.

-Backups y migraciones

-Scripts para exportar/importar datos de la base de datos.



Tareas que haría con IA:

-Generación de código

-Crear clases, funciones, o incluso prototipos completos de nuevas funcionalidades.

-Refactorización automática de código.

-Generación de pruebas unitarias

-IA puede leer tu código y sugerir tests que cubran escenarios extremos que podrías olvidar.

-Sugerir mocks o inputs complejos para el menú interactivo.

-Documentación automática

-Crear README.md actualizado con funcionalidades detectadas en el código.

-Generar documentación técnica (docs/) explicando flujo, clases y relaciones.

-Validación de reglas de la biblioteca

-Revisar que los flujos de préstamo/devolución cumplan con las reglas (por ejemplo, evitar préstamos duplicados, calcular retrasos, multas).

-Optimización de flujo

-Detectar puntos donde el código se puede simplificar o modularizar.

-Sugerir mejoras de UX en menús y mensajes de consola.

-Análisis predictivo

-IA podría analizar el historial de préstamos para predecir libros populares o detectar usuarios morosos.

-Crear un chatbot que ayude al bibliotecario:
Ej.: “¿Qué libros están vencidos?” o “Registrar un nuevo usuario”.
