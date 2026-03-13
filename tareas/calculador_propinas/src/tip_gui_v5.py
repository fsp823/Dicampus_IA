#!/usr/bin/env python3
# tip_gui.py
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk

# Intentar importar la función desde src; si falla, añadir la raíz del proyecto al path
try:
    from src.tip_cli_v5 import calcular_propina, format_currency_usd
except Exception:
    ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT))
    from src.tip_cli_v5 import calcular_propina, format_currency_usd

def actualizar(*_):
    error_var.set("")
    try:
        bill = bill_var.get().strip()
        pct = pct_var.get().strip()
        people = people_var.get().strip()

        tip, total, per_person = calcular_propina(bill or "0", pct or "10", people or "1")

        tip_var.set(format_currency_usd(tip))
        total_var.set(format_currency_usd(total))
        per_var.set(format_currency_usd(per_person))
    except ValueError as ve:
        tip_var.set("—")
        total_var.set("—")
        per_var.set("—")
        error_var.set(str(ve))
    except Exception as e:
        tip_var.set("—")
        total_var.set("—")
        per_var.set("—")
        error_var.set("Error inesperado: " + str(e))

def reset():
    bill_var.set("0.00")
    pct_var.set("10")
    people_var.set("1")
    actualizar()

root = tk.Tk()
root.title("Calculadora de Propinas (USD)")

frm = ttk.Frame(root, padding=16)
frm.grid(sticky="nsew")

ttk.Label(frm, text="Valor de la factura").grid(column=0, row=0, sticky="w")
bill_var = tk.StringVar(value="0.00")
bill_entry = ttk.Entry(frm, textvariable=bill_var, width=20)
bill_entry.grid(column=0, row=1, pady=6, sticky="we")

ttk.Label(frm, text="Porcentaje (%)").grid(column=0, row=2, sticky="w")
pct_var = tk.StringVar(value="10")
pct_entry = ttk.Entry(frm, textvariable=pct_var, width=20)
pct_entry.grid(column=0, row=3, pady=6, sticky="we")

ttk.Label(frm, text="Dividir entre (personas)").grid(column=0, row=4, sticky="w")
people_var = tk.StringVar(value="1")
people_entry = ttk.Entry(frm, textvariable=people_var, width=20)
people_entry.grid(column=0, row=5, pady=6, sticky="we")

btn_frame = ttk.Frame(frm)
btn_frame.grid(column=0, row=6, pady=10, sticky="we")
calc_btn = ttk.Button(btn_frame, text="Calcular", command=actualizar)
calc_btn.pack(side="left", padx=(0, 8))
reset_btn = ttk.Button(btn_frame, text="Limpiar", command=reset)
reset_btn.pack(side="left")

ttk.Separator(frm, orient="horizontal").grid(column=0, row=7, sticky="we", pady=8)

tip_var = tk.StringVar(value="$0.00")
total_var = tk.StringVar(value="$0.00")
per_var = tk.StringVar(value="$0.00")
error_var = tk.StringVar(value="")

ttk.Label(frm, text="Propina:").grid(column=0, row=8, sticky="w")
ttk.Label(frm, textvariable=tip_var).grid(column=0, row=9, sticky="e")

ttk.Label(frm, text="Total:").grid(column=0, row=10, sticky="w")
ttk.Label(frm, textvariable=total_var).grid(column=0, row=11, sticky="e")

ttk.Label(frm, text="Por persona:").grid(column=0, row=12, sticky="w")
ttk.Label(frm, textvariable=per_var).grid(column=0, row=13, sticky="e")

error_label = ttk.Label(frm, textvariable=error_var, foreground="red")
error_label.grid(column=0, row=14, pady=(8, 0), sticky="we")

for var in (bill_var, pct_var, people_var):
    var.trace_add("write", actualizar)

root.columnconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
bill_entry.focus()
actualizar()

if __name__ == "__main__":
    root.mainloop()
