import unittest
import sys
import os

# Añadir la carpeta src al path para poder importar el módulo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


from validar_email import validar_email


class TestValidarEmail(unittest.TestCase):

    # Email válido
    def test_email_valido(self):
        self.assertTrue(validar_email("usuario@email.com"))

    # Falta @
    def test_sin_arroba(self):
        self.assertFalse(validar_email("usuarioemail.com"))

    # Falta punto
    def test_sin_punto(self):
        self.assertFalse(validar_email("usuario@emailcom"))

    # Falta ambos
    def test_sin_ninguno(self):
        self.assertFalse(validar_email("usuarioemailcom"))

    # Caso límite: texto vacío
    def test_email_vacio(self):
        self.assertFalse(validar_email(""))


if __name__ == "__main__":
    unittest.main()