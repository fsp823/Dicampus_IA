from app import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(3, 5) == 8
    assert sumar(0, 0) == 0
    assert sumar(10, 1) == 11

def test_restar():
    assert restar(10, 4) == 6
    assert restar(5, 5) == 0
    assert restar(7, 2) == 5

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(0, 7) == 0
    assert multiplicar(5, 5) == 25

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3
    assert dividir(5, 0) == "Error: no se puede dividir entre cero."
