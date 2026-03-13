#!/usr/bin/env python3
"""
Calculadora de propinas (GUI con Tkinter).
Permite cambiar porcentaje y dividir entre personas.
"""

import tkinter as tk
from tkinter import ttk

def formato_eur(value: float) -> str:
    return f"{value:,.2f} €"

def calcular():
    try:
        bill = float(bill_var.get().replace(',', '.'))
    except ValueError:
        bill = 0.0
    try:
        pct = float(pct_var.get().replace(',', '.'))
    except ValueError:
        pct = 10.0
    try:
        people = int(people_var.get())
        if people < 1:
            people = 1
    except ValueError:
        people = 1

    tip = bill * (pct / 100.0)
    total = bill + tip
    per_person = total / people

    tip_label_var.set(formato_eur(tip))
    total_label_var.set(formato_eur(total))
    per_label_var.set(formato_eur(per_person))

root = tk.Tk()
root.title("Calculadora de Propinas 10%")

frm = ttk.Frame(root, padding=16)
frm.grid()

ttk.Label(frm, text="Valor de la factura (€)").grid(column=0, row=0, sticky="w")
bill_var = tk.StringVar(value="0.00")
ttk.Entry(frm, textvariable=bill_var, width=20).grid(column=0, row=1, pady=6)

ttk.Label(frm, text="Porcentaje (%)").grid(column=0, row=2, sticky="w")
pct_var = tk.StringVar(value="10")
ttk.Entry(frm, textvariable=pct_var, width=20).grid(column=0, row=3, pady=6)

ttk.Label(frm, text="Dividir entre (personas)").grid(column=0, row=4, sticky="w")
people_var = tk.StringVar(value="1")
ttk.Entry(frm, textvariable=people_var, width=20).grid(column=0, row=5, pady=6)

calc_btn = ttk.Button(frm, text="Calcular", command=calcular)
calc_btn.grid(column=0, row=6, pady=10)

tip_label_var = tk.StringVar(value="0.00 €")
total_label_var = tk.StringVar(value="0.00 €")
per_label_var = tk.StringVar(value="0.00 €")

ttk.Label(frm, text="Propina:").grid(column=0, row=7, sticky="w")
ttk.Label(frm, textvariable=tip_label_var).grid(column=0, row=8, sticky="e")

ttk.Label(frm, text="Total:").grid(column=0, row=9, sticky="w")
ttk.Label(frm, textvariable=total_label_var).grid(column=0, row=10, sticky="e")

ttk.Label(frm, text="Por persona:").grid(column=0, row=11, sticky="w")
ttk.Label(frm, textvariable=per_label_var).grid(column=0, row=12, sticky="e")

root.mainloop()
