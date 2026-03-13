# src/tip_cli.py
from typing import Tuple, Optional
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
import locale

def _to_decimal(value, name: str) -> Decimal:
    try:
        s = str(value).strip().replace(',', '.')
        return Decimal(s)
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError(f"{name} no es un número válido") from e

def calcular_propina(bill, porcentaje: float = 10.0, people: int = 1, fixed_tip: Optional[float] = None) -> Tuple[float, float, float]:
    """
    Calcula la propina, el total y el importe por persona.

    Parámetros
    - bill: importe de la factura (>= 0). Se aceptan números o strings con coma o punto.
    - porcentaje: porcentaje de propina (>= 0). Se aceptan números o strings con coma o punto.
    - people: número de personas (entero >= 1). Se aceptan enteros o strings que representen enteros.
    - fixed_tip: si se proporciona (no None), se usa este monto fijo de propina en la misma moneda
                 en lugar de calcularla por porcentaje. Se aceptan números o strings.

    Devuelve (tip, total, per_person) como floats redondeados a 2 decimales.
    Lanza ValueError con mensajes claros si alguna entrada es inválida.
    """
    bill_d = _to_decimal(bill, "Factura")
    if bill_d < 0:
        raise ValueError("La factura debe ser un número positivo o cero")

    # Validar people como entero
    try:
        people_i = int(str(people))
    except Exception as e:
        raise ValueError("Número de personas debe ser un entero") from e
    if people_i < 1:
        raise ValueError("Número de personas debe ser >= 1")

    # Si fixed_tip se proporciona, usarlo (validar)
    if fixed_tip is not None:
        fixed_d = _to_decimal(fixed_tip, "Propina fija")
        if fixed_d < 0:
            raise ValueError("La propina fija debe ser >= 0")
        tip_d = fixed_d.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    else:
        pct_d = _to_decimal(porcentaje, "Porcentaje")
        if pct_d < 0:
            raise ValueError("El porcentaje debe ser >= 0")
        tip_d = (bill_d * (pct_d / Decimal('100'))).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    total_d = (bill_d + tip_d).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    per_person_d = (total_d / Decimal(people_i)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    return float(tip_d), float(total_d), float(per_person_d)

# -------------------------
# Formateo de moneda local
# -------------------------
def _try_babel_format(amount, currency_code, locale_str):
    try:
        from babel.numbers import format_currency
    except Exception:
        return None
    try:
        return format_currency(amount, currency_code, locale=locale_str)
    except Exception:
        return None

def _locale_currency_fallback(amount):
    try:
        locale.setlocale(locale.LC_ALL, '')
    except Exception:
        pass
    try:
        return locale.currency(amount, symbol=True, grouping=True)
    except Exception:
        return f"${amount:,.2f}"

def format_currency_local(amount) -> str:
    try:
        d = _to_decimal(amount, "Cantidad")
    except ValueError as e:
        raise ValueError("Cantidad no es un número válido") from e
    d_q = d.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    loc = None
    try:
        loc = locale.getdefaultlocale()[0]
    except Exception:
        loc = None

    if loc:
        currency_candidates = []
        if loc.lower().startswith(('es', 'fr', 'de')):
            currency_candidates = ['EUR', 'USD']
        elif loc.lower().startswith('en_us') or loc.lower().startswith('en'):
            currency_candidates = ['USD', 'EUR']
        else:
            currency_candidates = ['USD', 'EUR']

        for code in currency_candidates:
            s = _try_babel_format(float(d_q), code, loc)
            if s:
                return s

    try:
        return _locale_currency_fallback(float(d_q))
    except Exception:
        return f"${float(d_q):,.2f}"
