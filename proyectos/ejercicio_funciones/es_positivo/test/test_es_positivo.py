
import unittest

import src.es_positivo

def es_positivo(numero):
    """
    Devuelve True si el número es mayor que 0.
    En caso contrario devuelve False.
    """
    return numero > 0



class TestEsPositivo(unittest.TestCase):

    # Casos positivos
    def test_numero_positivo_entero(self):
        self.assertTrue(es_positivo(5))

    def test_numero_positivo_flotante(self):
        self.assertTrue(es_positivo(0.1))

    # Casos negativos
    def test_numero_negativo_entero(self):
        self.assertFalse(es_positivo(-5))

    def test_numero_negativo_flotante(self):
        self.assertFalse(es_positivo(-0.1))

    # Casos límite
    def test_cero(self):
        self.assertFalse(es_positivo(0))

    def test_cero_flotante(self):
        self.assertFalse(es_positivo(0.0))

    def test_numero_muy_pequeno_positivo(self):
        self.assertTrue(es_positivo(1e-15))

    def test_numero_muy_pequeno_negativo(self):
        self.assertFalse(es_positivo(-1e-15))


if __name__ == "__main__":
    unittest.main()