import pytest
import sys
from pathlib import Path
import main


def run_main(monkeypatch, args, stdin_data=""):
    """
    Ejecuta main.main() simulando argumentos y stdin.
    Devuelve la salida capturada.
    """

    # Simular argumentos
    monkeypatch.setattr(sys, "argv", ["main.py"] + args)

    # Simular stdin
    monkeypatch.setattr(sys.stdin, "isatty", lambda: stdin_data == "")
    monkeypatch.setattr(sys.stdin, "read", lambda: stdin_data)

    # Capturar salida
    from io import StringIO
    salida = StringIO()
    monkeypatch.setattr(sys, "stdout", salida)

    main.main()
    return salida.getvalue()


# ---------------------------------------------------------
# TEST 1: Analizar archivo real
# ---------------------------------------------------------
def test_main_analiza_archivo(monkeypatch: pytest.MonkeyPatch, tmp_path: Path):
    archivo = tmp_path / "ejemplo.txt"
    archivo.write_text("hola mundo hola", encoding="utf-8")

    salida = run_main(monkeypatch, ["--archivo", str(archivo)])

    assert "Total de palabras: 3" in salida
    assert "hola" in salida
    assert "mundo" in salida


# ---------------------------------------------------------
# TEST 2: Archivo inexistente
# ---------------------------------------------------------
def test_main_archivo_inexistente(monkeypatch: pytest.MonkeyPatch):
    salida = run_main(monkeypatch, ["--archivo", "no_existe.txt"])
    assert "Error" in salida


# ---------------------------------------------------------
# TEST 3: Leer desde stdin
# ---------------------------------------------------------
def test_main_stdin(monkeypatch: pytest.MonkeyPatch):
    texto = "python python hola"
    salida = run_main(monkeypatch, [], stdin_data=texto)

    assert "Total de palabras: 3" in salida
    assert "python" in salida
    assert "hola" in salida


# ---------------------------------------------------------
# TEST 4: Sin archivo ni stdin
# ---------------------------------------------------------
def test_main_sin_entrada(monkeypatch: pytest.MonkeyPatch):
    salida = run_main(monkeypatch, [])
    assert "No se proporcionó texto" in salida
