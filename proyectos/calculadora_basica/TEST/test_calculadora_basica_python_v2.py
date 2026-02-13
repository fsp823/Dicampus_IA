import builtins
from calculadora_basica_python_v2 import main  # asumiendo que tu menú está en una función main()

def test_menu_suma(monkeypatch, capsys):
    # Simula la secuencia de entradas del usuario:
    # 1 → elegir "sumar"
    # 7 → primer número
    # 5 → segundo número
    # 5 → salir del programa
    inputs = iter(["1", "7", "5", "5"])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main()  # ejecuta el menú

    salida = capsys.readouterr().out
    assert "Resultado: 12" in salida


def test_menu_dividir_por_cero(monkeypatch, capsys):
    inputs = iter(["4", "10", "0", "5"])  # dividir 10 entre 0 y luego salir

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main()

    salida = capsys.readouterr().out
    assert "Error: no se puede dividir entre cero." in salida
