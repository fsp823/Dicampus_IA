# test/test_manual_unittest.py
import sys
import unittest
from pathlib import Path

# Asegura que la raíz del proyecto sea importable (para que 'src' funcione)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.tip_cli_v2 import calcular_propina

class TestCalculadoraPropinas(unittest.TestCase):
    def test_montos_positivos_y_calculo(self):
        cases = [
            (0.0, 10.0, 1),
            (1.23, 10.0, 1),
            (1000.0, 10.0, 4),
        ]
        for bill, pct, people in cases:
            with self.subTest(bill=bill, pct=pct, people=people):
                tip, total = calcular_propina(bill, pct)
                self.assertGreaterEqual(tip, 0.0, "La propina debe ser >= 0")
                self.assertGreaterEqual(total, 0.0, "El total debe ser >= 0")
                # comprobaciones aritméticas
                self.assertAlmostEqual(tip, bill * (pct / 100.0), places=9)
                self.assertAlmostEqual(total, bill + tip, places=9)
                # división por personas (comprobación auxiliar)
                per_person = total / people
                self.assertGreaterEqual(per_person, 0.0)

    def test_factura_negativa_lanza_value_error(self):
        with self.assertRaises(ValueError) as cm:
            calcular_propina(-5.0, 10.0)
        self.assertIn("factura", str(cm.exception).lower())

    def test_porcentaje_negativo_lanza_value_error(self):
        with self.assertRaises(ValueError) as cm:
            calcular_propina(50.0, -10.0)
        self.assertIn("porcentaje", str(cm.exception).lower())

    def test_entrada_no_numerica_manejada(self):
        # probar que cadenas no numéricas lanzan ValueError
        with self.assertRaises(ValueError):
            calcular_propina("no-num", 10.0)
        with self.assertRaises(ValueError):
            calcular_propina(50.0, "no-pct")

    def test_numero_personas_entero_positivo_validacion_manual(self):
        # Esta función no recibe 'people', así que validamos externamente
        def safe_divide(total, people):
            try:
                people_i = int(people)
            except Exception as e:
                raise ValueError("Número de personas debe ser un entero") from e
            if people_i < 1:
                raise ValueError("Número de personas debe ser >= 1")
            return total / people_i

        tip, total = calcular_propina(100.0, 10.0)
        # casos válidos
        self.assertAlmostEqual(safe_divide(total, 1), total)
        self.assertAlmostEqual(safe_divide(total, "2"), total / 2)

        # casos inválidos: deben lanzar ValueError
        for invalid in [0, -1, "0", "-3", 2.5, "3.7", "dos"]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    safe_divide(total, invalid)

    def test_try_except_handling_example(self):
        # ejemplo que demuestra manejo con try/except en el código de llamada
        error_caught = False
        try:
            calcular_propina("no-num", 10.0)
        except ValueError as e:
            error_caught = True
            self.assertTrue("no es un número" in str(e).lower() or "factura" in str(e).lower())
        self.assertTrue(error_caught, "Se esperaba capturar un ValueError")

if __name__ == "__main__":
    unittest.main()
