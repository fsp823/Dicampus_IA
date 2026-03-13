# test/test_manual_unittest.py
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.tip_cli_v3 import calcular_propina

class TestCalculadoraPropinas(unittest.TestCase):
    def test_montos_positivos_y_calculo(self):
        cases = [
            (0.0, 10.0, 1),
            ("1,23", "10", 1),
            (1000.0, 10.0, 4),
        ]
        for bill, pct, people in cases:
            with self.subTest(bill=bill, pct=pct, people=people):
                tip, total, per_person = calcular_propina(bill, pct, people)
                self.assertGreaterEqual(tip, 0.0, "La propina debe ser >= 0")
                self.assertGreaterEqual(total, 0.0, "El total debe ser >= 0")
                self.assertAlmostEqual(tip, float(str(bill).replace(',', '.')) * (float(str(pct).replace(',', '.')) / 100.0), places=9)
                self.assertAlmostEqual(total, float(str(bill).replace(',', '.')) + tip, places=9)
                self.assertAlmostEqual(per_person, total / int(str(people)), places=9)

    def test_factura_negativa_lanza_value_error(self):
        with self.assertRaises(ValueError) as cm:
            calcular_propina(-5.0, 10.0, 1)
        self.assertIn("factura", str(cm.exception).lower())

    def test_porcentaje_negativo_lanza_value_error(self):
        with self.assertRaises(ValueError) as cm:
            calcular_propina(50.0, -10.0, 1)
        self.assertIn("porcentaje", str(cm.exception).lower())

    def test_people_invalid_lanza_value_error(self):
        for invalid in [0, -1, "0", "-3", 2.5, "3.7", "dos"]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    calcular_propina(100.0, 10.0, invalid)

    def test_entrada_no_numerica_manejada(self):
        with self.assertRaises(ValueError):
            calcular_propina("no-num", 10.0, 1)
        with self.assertRaises(ValueError):
            calcular_propina(50.0, "no-pct", 1)

    def test_try_except_handling_example(self):
        error_caught = False
        try:
            calcular_propina("no-num", 10.0, 1)
        except ValueError as e:
            error_caught = True
            self.assertTrue("no es un número" in str(e).lower() or "factura" in str(e).lower())
        self.assertTrue(error_caught)

if __name__ == "__main__":
    unittest.main()
