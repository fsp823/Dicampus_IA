# src/tip_cli.py
from typing import Tuple

def calcular_propina(bill, porcentaje: float = 10.0, people: int = 1) -> Tuple[float, float, float]:
    """
    Calcula la propina, el total y el importe por persona.

    Parámetros
    - bill: importe de la factura (>= 0). Se aceptan números o strings con coma o punto.
    - porcentaje: porcentaje de propina (>= 0). Se aceptan números o strings con coma o punto.
    - people: número de personas (entero >= 1). Se aceptan enteros o strings que representen enteros.

    Devuelve
    - (tip, total, per_person)

    Lanza ValueError con mensajes claros si alguna entrada es inválida.
    """
    # Validar y convertir bill
    try:
        bill_f = float(str(bill).replace(',', '.'))
    except Exception as e:
        raise ValueError("Factura no es un número válido") from e
    if bill_f < 0:
        raise ValueError("La factura debe ser un número positivo o cero")

    # Validar y convertir porcentaje
    try:
        pct_f = float(str(porcentaje).replace(',', '.'))
    except Exception as e:
        raise ValueError("Porcentaje no es un número válido") from e
    if pct_f < 0:
        raise ValueError("El porcentaje debe ser >= 0")

    # Validar y convertir people (debe ser entero)
    try:
        # convertir a string primero para que "2" funcione y "2.0" falle
        people_i = int(str(people))
    except Exception as e:
        raise ValueError("Número de personas debe ser un entero") from e
    if people_i < 1:
        raise ValueError("Número de personas debe ser >= 1")

    tip = bill_f * (pct_f / 100.0)
    total = bill_f + tip
    per_person = total / people_i

    return tip, total, per_person
