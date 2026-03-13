# src/tip_cli.py
from typing import Tuple
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

def _to_decimal(value, name: str) -> Decimal:
    try:
        s = str(value).strip().replace(',', '.')
        return Decimal(s)
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError(f"{name} no es un número válido") from e

def calcular_propina(bill, porcentaje: float = 10.0, people: int = 1) -> Tuple[float, float, float]:
    """
    Calcula la propina, el total y el importe por persona usando redondeo humano (ROUND_HALF_UP).

    - bill: importe de la factura (>= 0). Se aceptan números o strings con coma o punto.
    - porcentaje: porcentaje de propina (>= 0). Se aceptan números o strings con coma o punto.
    - people: número de personas (entero >= 1). Se aceptan enteros o strings que representen enteros.

    Devuelve (tip, total, per_person) como floats redondeados a 2 decimales.
    Lanza ValueError con mensajes claros si alguna entrada es inválida.
    """
    # Convertir y validar bill
    bill_d = _to_decimal(bill, "Factura")
    if bill_d < 0:
        raise ValueError("La factura debe ser un número positivo o cero")

    # Convertir y validar porcentaje
    pct_d = _to_decimal(porcentaje, "Porcentaje")
    if pct_d < 0:
        raise ValueError("El porcentaje debe ser >= 0")

    # Validar people como entero
    try:
        people_i = int(str(people))
    except Exception as e:
        raise ValueError("Número de personas debe ser un entero") from e
    if people_i < 1:
        raise ValueError("Número de personas debe ser >= 1")

    # Cálculo con Decimal para evitar errores de float
    # tip = bill * (pct / 100)
    tip_d = (bill_d * (pct_d / Decimal('100'))).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    total_d = (bill_d + tip_d).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    per_person_d = (total_d / Decimal(people_i)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    # Devolver como floats (compatibilidad con tests existentes)
    return float(tip_d), float(total_d), float(per_person_d)
