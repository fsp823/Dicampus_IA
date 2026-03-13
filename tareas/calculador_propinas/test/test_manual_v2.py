# test/test_manual.py
import sys
from pathlib import Path
import math

# Hace importable la carpeta raíz del proyecto (para que 'src' funcione)
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.tip_cli import calcular_propina  # asume src/tip_cli.py existe

def safe_calculate(bill, porcentaje=10.0, people=1):
    """
    Valida entradas y llama a calcular_propina.
    - bill: número >= 0
    - porcentaje: número (se permite 0)
    - people: entero >= 1
    Devuelve (tip, total, per_person) o lanza ValueError.
    """
    # Validaciones
    try:
        # convertir y comprobar bill
        bill_f = float(str(bill).replace(',', '.'))
    except Exception as e:
        raise ValueError("Factura no es un número válido") from e
    if bill_f < 0:
        raise ValueError("La factura debe ser un número positivo o cero")

    # porcentaje: convertir a float
    try:
        pct_f = float(str(porcentaje).replace(',', '.'))
    except Exception as e:
        raise ValueError("Porcentaje no es un número válido") from e

    # people: debe ser entero positivo
    try:
        # aceptar strings que representen enteros
        people_i = int(people)
    except Exception as e:
        raise ValueError("Número de personas debe ser un entero") from e
    if people_i < 1:
        raise ValueError("Número de personas debe ser >= 1")

    # Llamada a la función real
    tip, total = calcular_propina(bill_f, pct_f)
    per_person = total / people_i

    return tip, total, per_person

# ---------- Tests (pytest style) ----------

def test_positive_amounts_and_calculation():
    # casos típicos
    cases = [
        (0.0, 10.0, 1),
        (1.23, 10.0, 1),
        (1000.0, 10.0, 4),
    ]
    for bill, pct, people in cases:
        tip, total, per = safe_calculate(bill, pct, people)
        # propina correcta
        assert math.isclose(tip, bill * (pct / 100.0), rel_tol=1e-9)
        # total correcto
        assert math.isclose(total, bill + tip, rel_tol=1e-9)
        # por persona correcto
        assert math.isclose(per, total / people, rel_tol=1e-9)
        # todos los montos no negativos
        assert tip >= 0
        assert total >= 0
        assert per >= 0

def test_negative_bill_raises_value_error():
    try:
        safe_calculate(-5.0, 10.0, 1)
        raised = False
    except ValueError as e:
        raised = True
        assert "factura" in str(e).lower() or "positivo" in str(e).lower()
    assert raised

def test_people_must_be_positive_integer():
    # cero personas
    for invalid in [0, -1, "0", "-3"]:
        try:
            safe_calculate(50.0, 10.0, invalid)
            raised = False
        except ValueError:
            raised = True
        assert raised

    # no entero (float string)
    for invalid in [2.5, "3.7", "dos"]:
        try:
            safe_calculate(50.0, 10.0, invalid)
            raised = False
        except ValueError:
            raised = True
        assert raised

def test_try_except_handling_example():
    # ejemplo de manejo con try/except: la prueba comprueba que el bloque captura el error
    error_caught = False
    try:
        # entrada inválida intencional
        safe_calculate("no-num", 10.0, 1)
    except ValueError as e:
        error_caught = True
        # mensaje útil para el usuario
        assert "no es un número" in str(e).lower() or "factura" in str(e).lower()
    assert error_caught

# Permite ejecutar el archivo directamente sin pytest
if __name__ == "__main__":
    tests = [
        test_positive_amounts_and_calculation,
        test_negative_bill_raises_value_error,
        test_people_must_be_positive_integer,
        test_try_except_handling_example,
    ]
    for t in tests:
        try:
            t()
            print(f"{t.__name__}: OK")
        except AssertionError as ae:
            print(f"{t.__name__}: FALLÓ -> {ae}")
        except Exception as ex:
            print(f"{t.__name__}: ERROR inesperado -> {ex}")
