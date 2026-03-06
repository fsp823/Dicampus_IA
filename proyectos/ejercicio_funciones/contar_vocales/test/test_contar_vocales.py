import unittest
import sys
import os

# Añadir carpeta src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from contar_vocales import contar_vocales


class TestContarVocales(unittest.TestCase):

    # Caso normal
    def test_frase_normal(self):
        self.assertEqual(contar_vocales("hola mundo"), 4)

    # Mayúsculas
    def test_mayusculas(self):
        self.assertEqual(contar_vocales("HOLA MUNDO"), 4)

    # Mezcla de mayúsculas y minúsculas
    def test_mixto(self):
        self.assertEqual(contar_vocales("HoLa MuNdO"), 4)

    # Vocales con acento
    def test_vocales_con_acento(self):
        self.assertEqual(contar_vocales("áéíóú"), 5)

    # Vocales con diéresis
    def test_dieresis(self):
        self.assertEqual(contar_vocales("pingüino"), 4)

    # Solo consonantes
    def test_solo_consonantes(self):
        self.assertEqual(contar_vocales("bcdfghjklmnpqrstvwxyz"), 0)

    # Texto vacío (caso límite)
    def test_texto_vacio(self):
        self.assertEqual(contar_vocales(""), 0)

    # Espacios
    def test_solo_espacios(self):
        self.assertEqual(contar_vocales("     "), 0)

    # Números
    def test_numeros(self):
        self.assertEqual(contar_vocales("1234567890"), 0)

    # Caracteres especiales
    def test_caracteres_especiales(self):
        self.assertEqual(contar_vocales("!@#$%^&*()"), 0)

    # Letras sueltas
    def test_letras_sueltas(self):
        self.assertEqual(contar_vocales("a b c d e"), 2)

    # Frase con acentos
    def test_frase_con_acentos(self):
        self.assertEqual(contar_vocales("Programación en Python"), 7)


if __name__ == "__main__":
    unittest.main()