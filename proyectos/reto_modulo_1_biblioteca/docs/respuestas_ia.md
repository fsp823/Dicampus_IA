Si **Talento Solutions** quiere probar cómo la IA puede ayudar a programar un sistema sencillo de biblioteca, lo ideal es empezar con un sistema mínimo funcional (MVP) y luego escalar.

A continuación te muestro cómo podría diseñarse y cómo la IA puede intervenir en cada parte.

---

# 📚 Sistema básico de gestión de biblioteca

## 1️⃣ Funcionalidades mínimas

Un sistema sencillo debería permitir:

### 📖 Gestión de libros

* Agregar libro
* Editar libro
* Eliminar libro
* Listar libros
* Buscar por título, autor o ISBN

### 👤 Gestión de usuarios

* Registrar usuario
* Editar usuario
* Listar usuarios

### 🔄 Gestión de préstamos

* Registrar préstamo
* Registrar devolución
* Ver préstamos activos
* Historial de préstamos

---

# 🧠 ¿Cómo ayuda la IA en este proyecto?

IA puede ayudar en:

1. Generación de código base
2. Diseño de base de datos
3. Generación automática de pruebas
4. Validación de reglas de negocio
5. Documentación automática
6. Asistente interno para bibliotecarios

---

# 🗄️ Diseño simple de base de datos

Ejemplo relacional:

### 📘 Tabla: Libros

* id
* titulo
* autor
* isbn
* año
* disponible (boolean)

### 👤 Tabla: Usuarios

* id
* nombre
* email
* telefono

### 📅 Tabla: Prestamos

* id
* libro_id
* usuario_id
* fecha_prestamo
* fecha_devolucion
* estado

---

# 💻 Ejemplo simple en Python (versión consola)

Aquí un ejemplo básico orientado a objetos:

```python
class Libro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, libro_id, usuario_id):
        libro = next((l for l in self.libros if l.id == libro_id and l.disponible), None)
        if libro:
            libro.disponible = False
            self.prestamos.append((libro_id, usuario_id))
            print("Préstamo registrado")
        else:
            print("Libro no disponible")

    def devolver_libro(self, libro_id):
        libro = next((l for l in self.libros if l.id == libro_id), None)
        if libro:
            libro.disponible = True
            print("Libro devuelto")
```

Esto sería un prototipo inicial.

---

# 🚀 Escalando el sistema

Para una versión más realista:

* Backend: FastAPI o Django
* Base de datos: PostgreSQL
* Frontend: React o Vue
* Autenticación con roles (bibliotecario / administrador)
* API REST

---

# 🤖 Ejemplos concretos donde la IA agrega valor

### 1️⃣ Recomendador de libros

* Basado en historial de préstamos

### 2️⃣ Chatbot interno

* “¿Qué libros están vencidos?”
* “¿Qué usuario tiene más préstamos activos?”

### 3️⃣ Detección de morosos

* Predicción de retrasos

### 4️⃣ OCR para registrar libros

* Escaneo de ISBN desde cámara

---

# 📊 Roadmap sugerido para Talento Solutions

Fase 1 – MVP (2 semanas)

* CRUD de libros
* CRUD de usuarios
* Registro de préstamos

Fase 2 – API + Web (3–4 semanas)

* Backend REST
* Base de datos real
* Interfaz web simple

Fase 3 – IA aplicada (4 semanas)

* Recomendador
* Asistente conversacional
* Reportes automáticos

---

Si quieres, puedo:

* 🔹 Diseñar la arquitectura completa tipo empresa
* 🔹 Generar el backend completo en FastAPI
* 🔹 Crear el modelo de base de datos listo para PostgreSQL
* 🔹 Hacer un demo más avanzado con reglas reales (multas, vencimientos, etc.)
* 🔹 Armar un pitch técnico para presentar a dirección

¿Talento Solutions quiere algo tipo demo rápido o proyecto serio escalable?

Perfecto. Aquí tienes el proyecto completo con la estructura solicitada.

---

# 📁 Estructura del proyecto

```
biblioteca-ia/
│
├── src/
│   └── biblioteca.py
│
├── tests/
│   └── test_biblioteca.py
│
├── docs/
│   └── proceso_ia.md
│
├── README.md
├── .gitignore
└── requirements.txt
```

---

# 📄 src/biblioteca.py

```python
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
```

---

# 📄 tests/test_biblioteca.py

```python
import pytest
from src.biblioteca import Biblioteca, Libro, Usuario


def setup_biblioteca():
    biblioteca = Biblioteca()
    libro = Libro(1, "Clean Code", "Robert C. Martin", "123456")
    usuario = Usuario(1, "Juan Pérez", "juan@email.com")
    biblioteca.agregar_libro(libro)
    biblioteca.agregar_usuario(usuario)
    return biblioteca


def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro(1, "Test", "Autor", "111")
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1


def test_prestar_libro():
    biblioteca = setup_biblioteca()
    prestamo = biblioteca.prestar_libro("123456", 1)
    assert prestamo.libro.disponible is False
    assert len(biblioteca.prestamos_activos()) == 1


def test_devolver_libro():
    biblioteca = setup_biblioteca()
    biblioteca.prestar_libro("123456", 1)
    biblioteca.devolver_libro("123456")
    assert len(biblioteca.prestamos_activos()) == 0


def test_no_prestar_libro_no_disponible():
    biblioteca = setup_biblioteca()
    biblioteca.prestar_libro("123456", 1)
    with pytest.raises(ValueError):
        biblioteca.prestar_libro("123456", 1)


def test_no_agregar_libro_duplicado():
    biblioteca = Biblioteca()
    libro1 = Libro(1, "Libro A", "Autor", "999")
    libro2 = Libro(2, "Libro B", "Autor", "999")
    biblioteca.agregar_libro(libro1)
    with pytest.raises(ValueError):
        biblioteca.agregar_libro(libro2)
```

---

# 📄 docs/proceso_ia.md

```markdown
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
```

---

# 📄 README.md

````markdown
# Sistema de Gestión de Biblioteca

Proyecto demo desarrollado en Python para gestionar:

- Libros
- Usuarios
- Préstamos
- Devoluciones

## Requisitos

Python 3.10+

## Instalación

```bash
pip install -r requirements.txt
````

## Ejecutar pruebas

```bash
pytest
```

## Estructura

* src/ → Código fuente
* tests/ → Pruebas unitarias
* docs/ → Documentación del proceso IA

## Posibles mejoras

* Base de datos (PostgreSQL)
* API REST
* Interfaz web
* Sistema de multas

```

---

# 📄 requirements.txt

```

pytest>=7.0.0

```

---

# 📄 .gitignore

```

**pycache**/
*.pyc
*.pyo
*.pyd
.env
.venv
venv/
.env/
dist/
build/
*.egg-info/
.pytest_cache/

```

---

Si quieres, puedo ahora:

- 🔹 Convertirlo en API REST con FastAPI  
- 🔹 Añadir persistencia con SQLite  
- 🔹 Agregar sistema de multas por retraso  
- 🔹 Dockerizar el proyecto  
- 🔹 Prepararlo como proyecto técnico para evaluación de candidatos  

¿Quieres que lo llevemos a nivel “empresa real” ahora? 🚀
```

Perfecto. Aquí tienes **5 historias de usuario** y un diagrama de flujo del proceso de préstamo en texto.

---

# 📚 Historias de Usuario – Sistema de Biblioteca

## 1️⃣ Registrar libro

**Como** bibliotecario
**Quiero** registrar un nuevo libro en el sistema
**Para** que pueda estar disponible para préstamos

**Criterios de aceptación:**

* Se deben ingresar: título, autor, ISBN.
* No se permite registrar libros con ISBN duplicado.
* El libro queda marcado como "disponible" por defecto.

---

## 2️⃣ Registrar usuario

**Como** bibliotecario
**Quiero** registrar un nuevo usuario
**Para** que pueda solicitar préstamos

**Criterios de aceptación:**

* Se deben ingresar: nombre y email.
* No se permiten emails duplicados.
* El usuario queda activo automáticamente.

---

## 3️⃣ Prestar libro

**Como** bibliotecario
**Quiero** registrar el préstamo de un libro a un usuario
**Para** llevar control de los libros prestados

**Criterios de aceptación:**

* El libro debe existir en el sistema.
* El libro debe estar disponible.
* El usuario debe existir.
* El sistema registra fecha de préstamo.
* El libro cambia su estado a "no disponible".

---

## 4️⃣ Registrar devolución

**Como** bibliotecario
**Quiero** registrar la devolución de un libro
**Para** actualizar su disponibilidad

**Criterios de aceptación:**

* Debe existir un préstamo activo del libro.
* Se registra fecha de devolución.
* El libro cambia a "disponible".
* El préstamo deja de estar activo.

---

## 5️⃣ Consultar préstamos activos

**Como** bibliotecario
**Quiero** ver la lista de préstamos activos
**Para** identificar libros actualmente prestados

**Criterios de aceptación:**

* Se muestran solo préstamos sin devolución registrada.
* Se visualiza: libro, usuario, fecha de préstamo.
* Puede filtrarse por usuario.

---

# 🔄 Diagrama de Flujo – Proceso de Préstamo (Texto)

```
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
```

---

Si quieres, puedo:

* 🔹 Convertir el diagrama a formato Mermaid
* 🔹 Generar diagrama de casos de uso
* 🔹 Crear diagrama de clases UML
* 🔹 Agregar flujo alternativo con multas por retraso

¿Lo necesitas más orientado a documentación académica o a presentación ejecutiva?


hazme pruebas unitarias incluyendo el menú de consola


Perfecto. Aquí tienes una versión extendida de `src/biblioteca.py` que incluye un menú interactivo por consola para gestionar libros, usuarios y préstamos.

Reemplaza el contenido actual de `biblioteca.py` por este:

---

# 📄 src/biblioteca.py

```python
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
```

---

## ▶️ Cómo ejecutarlo

Desde la raíz del proyecto:

```bash
python src/biblioteca.py
```

---

Si quieres, puedo ahora:

* Añadir persistencia en archivo JSON (para que no se pierdan los datos al cerrar)
* Añadir validación de email
* Añadir fechas de vencimiento y multas
* Convertir el menú en interfaz tipo TUI más profesional

¿Quieres que lo hagamos más “realista” o lo dejamos como demo didáctica?


Perfecto. Aquí tienes **5 test unitarios** para el sistema, listos para usar con `pytest`.

Guárdalos en:

```
tests/test_biblioteca.py
```

---

# 📄 tests/test_biblioteca.py

```python
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
```

---

## ▶️ Ejecutar los tests

Desde la raíz del proyecto:

```bash
pytest
```

---

Si quieres, puedo generar ahora:

* Tests para el menú de consola (mocking input/output)
* Tests con cobertura avanzada
* Tests parametrizados
* Tests de integración simulando múltiples usuarios

¿Quieres que lo llevemos a nivel más profesional (por ejemplo, con coverage >90%)? 🚀
