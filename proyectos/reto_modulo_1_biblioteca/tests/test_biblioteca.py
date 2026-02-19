import pytest
from src import biblioteca
## from src.biblioteca_v3 import Biblioteca, Libro, Usuario, main
##from src.biblioteca_v3 import Biblioteca, Libro, Usuario,main
import src.biblioteca as biblioteca


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
