#!/usr/bin/env python3
"""
Calculadora de propinas (CLI) — calcula 10% y muestra total.
Uso: python tip_cli.py
"""

def calcular_propina(bill: float, porcentaje: float = 10.0) -> tuple:
    """Devuelve (propina, total). porcentaje en % (por ejemplo 10.0)."""
    tip = bill * (porcentaje / 100.0)
    total = bill + tip
    return tip, total

def formato_eur(value: float) -> str:
    return f"{value:,.2f} €"

def main():
    try:
        entrada = input("Introduce el valor de la factura (€): ").strip().replace(',', '.')
        bill = float(entrada)
        if bill < 0:
            print("El valor de la factura debe ser mayor o igual a 0.")
            return
    except ValueError:
        print("Entrada no válida. Introduce un número, por ejemplo 42.50")
        return

    porcentaje = 10.0  # fijo al 10%
    tip, total = calcular_propina(bill, porcentaje)

    print(f"Propina ({porcentaje:.0f}%): {formato_eur(tip)}")
    print(f"Total: {formato_eur(total)}")

if __name__ == "__main__":
    print(calcular_propina(50)) 
    main()
