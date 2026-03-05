import unittest
from src.capitalizar import capitalizar


class TestCapitalizar(unittest.TestCase):

    # Caso normal
    def test_texto_normal(self):
        self.assertEqual(capitalizar("hola mundo"), "Hola Mundo")

    # Texto ya capitalizado
    def test_texto_ya_capitalizado(self):
        self.assertEqual(capitalizar("Hola Mundo"), "Hola Mundo")

    # Texto en mayúsculas
    def test_texto_mayusculas(self):
        self.assertEqual(capitalizar("HOLA MUNDO"), "Hola Mundo")

    # Texto vacío (caso límite)
    def test_texto_vacio(self):
        self.assertEqual(capitalizar(""), "Texto vacío")

    # Una sola palabra
    def test_una_palabra(self):
        self.assertEqual(capitalizar("python"), "Python")


if __name__ == "__main__":
    unittest.main()