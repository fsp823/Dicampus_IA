import unittest
import sys
import os

# Añadir src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from resumen_usuario import resumen_usuario


class TestResumenUsuario(unittest.TestCase):

    def test_email_valido(self):
        resultado = resumen_usuario("juan perez", "juan@email.com")
        self.assertEqual(resultado, "Usuario: Juan Perez - Email correcto")

    def test_email_invalido(self):
        resultado = resumen_usuario("juan perez", "juanemail.com")
        self.assertEqual(resultado, "Usuario: Juan Perez - Email inválido")

    def test_nombre_mayusculas(self):
        resultado = resumen_usuario("JUAN PEREZ", "juan@email.com")
        self.assertEqual(resultado, "Usuario: Juan Perez - Email correcto")

    def test_nombre_minusculas(self):
        resultado = resumen_usuario("juan", "juan@email.com")
        self.assertEqual(resultado, "Usuario: Juan - Email correcto")


if __name__ == "__main__":
    unittest.main()