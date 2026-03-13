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
    Calcula la propina, el total y el importe por persona usando redondeo humano.

    Calcula la propina a partir de un importe de factura y un porcentaje, o bien
    acepta una **propina fija** si se proporciona `fixed_tip`. Todos los cálculos
    usan `decimal.Decimal` con `ROUND_HALF_UP` y los resultados se devuelven como
    `float` redondeados a dos decimales.

    Parameters
    ----------
    bill : int | float | str
        Importe de la factura. Se aceptan números o cadenas con coma o punto
        decimal (por ejemplo, `"12.34"` o `"12,34"`). Debe ser >= 0.
    porcentaje : int | float | str, optional
        Porcentaje de propina a aplicar (por defecto 10.0). Se aceptan números
        o cadenas con coma/punto. Ignorado si `fixed_tip` no es `None`.
    people : int | str, optional
        Número de personas para dividir el total (por defecto 1). Debe ser un
        entero >= 1; se aceptan cadenas que representen enteros válidos.
    fixed_tip : int | float | str | None, optional
        Monto absoluto de propina a usar en lugar del porcentaje. Si se
        proporciona, debe ser >= 0. Se aceptan números o cadenas con coma/punto.

    Returns
    -------
    tip : float
        Importe de la propina, redondeado a 2 decimales.
    total : float
        Suma de la factura más la propina, redondeada a 2 decimales.
    per_person : float
        Importe por persona (total dividido entre `people`), redondeado a 2 decimales.

    Raises
    ------
    ValueError
        Si `bill`, `porcentaje` o `fixed_tip` no son numéricos válidos o son
        negativos; si `people` no es un entero o es menor que 1.

    Examples
    --------
    >>> calcular_propina(100, 15, 2)
    (15.0, 115.0, 57.5)
    >>> calcular_propina("100,00", "10", "4")
    (10.0, 110.0, 27.5)
    >>> calcular_propina(80, fixed_tip="5")
    (5.0, 85.0, 85.0)

    Notes
    -----
    - Internamente se usa `decimal.Decimal` y `ROUND_HALF_UP` para evitar
      imprecisiones de punto flotante y aplicar el **redondeo humano**.
    - La función devuelve `float` para mantener compatibilidad con llamadas
      existentes; si se necesita precisión monetaria persistente, considere
      trabajar con `Decimal` en la capa superior.
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
