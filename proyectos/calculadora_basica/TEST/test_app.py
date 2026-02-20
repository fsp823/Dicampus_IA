import unittest
from src.app import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 5), 8)
        self.assertEqual(sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)
        self.assertEqual(restar(5, 5), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(0, 7), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 0), "Error: no se puede dividir entre cero.")

if __name__ == "__main__":
    unittest.main()
