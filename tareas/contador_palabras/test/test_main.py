import pytest
import sys
from pathlib import Path

# Añadir la raíz del proyecto al path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

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
def test_main_analiza_archivo(monkeypatch, tmp_path):
    archivo = tmp_path / "ejemplo.txt"
    archivo.write_text("hola mundo hola", encoding="utf-8")

    salida = run_main(monkeypatch, ["--archivo", str(archivo)])

    assert "Total de palabras: 3" in salida
    assert "hola" in salida
    assert "mundo" in salida


# ---------------------------------------------------------
# TEST 2: Archivo inexistente
# ---------------------------------------------------------
def test_main_archivo_inexistente(monkeypatch):
    salida = run_main(monkeypatch, ["--archivo", "no_existe.txt"])
    assert "Error" in salida


# ---------------------------------------------------------
# TEST 3: Leer desde stdin
# ---------------------------------------------------------
def test_main_stdin(monkeypatch):
    texto = "python python hola"
    salida = run_main(monkeypatch, [], stdin_data=texto)

    assert "Total de palabras: 3" in salida
    assert "python" in salida
    assert "hola" in salida


# ---------------------------------------------------------
# TEST 4: Sin archivo ni stdin
# ---------------------------------------------------------
def test_main_sin_entrada(monkeypatch):
    salida = run_main(monkeypatch, [])
    assert "No se proporcionó texto" in salida




if __name__ == "__main__":
    import pytest
    from _pytest.config import Config
    from _pytest.main import Session

    print("\nEjecutando tests...\n")

    # Ejecutar pytest y capturar estadísticas
    resultado = pytest.main(["--maxfail=1", "-q"])

    # Mostrar mensaje final
    if resultado == 0:
        print("\n✅ Todos los tests pasaron correctamente")
    else:
        print(f"\n❌ Algunos tests fallaron (código de salida: {resultado})")