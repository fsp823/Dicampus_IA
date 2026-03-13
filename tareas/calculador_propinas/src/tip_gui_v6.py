#!/usr/bin/env python3
# tip_gui.py
import sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk

# Intentar importar desde src; si falla, añadir la raíz del proyecto al path
try:
    from src.tip_cli_v6 import calcular_propina, format_currency_local
except Exception:
    ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(ROOT))
    from src.tip_cli_v6 import calcular_propina, format_currency_local

def actualizar(*_):
    error_var.set("")
    try:
        bill = bill_var.get().strip() or "0"
        mode = mode_var.get()  # 'pct' o 'fixed'
        pct = pct_var.get().strip() or "10"
        fixed = fixed_var.get().strip() or "0"
        people = people_var.get().strip() or "1"

        if mode == 'fixed':
            # pasar fixed_tip como keyword argument
            tip, total, per_person = calcular_propina(bill, porcentaje=10, people=people, fixed_tip=fixed)
        else:
            tip, total, per_person = calcular_propina(bill, porcentaje=pct, people=people)

        tip_var.set(format_currency_local(tip))
        total_var.set(format_currency_local(total))
        per_var.set(format_currency_local(per_person))
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
    fixed_var.set("0.00")
    people_var.set("1")
    mode_var.set('pct')
    actualizar()

root = tk.Tk()
root.title("Calculadora de Propinas")

frm = ttk.Frame(root, padding=16)
frm.grid(sticky="nsew")

# Factura
ttk.Label(frm, text="Valor de la factura").grid(column=0, row=0, sticky="w")
bill_var = tk.StringVar(value="0.00")
bill_entry = ttk.Entry(frm, textvariable=bill_var, width=20)
bill_entry.grid(column=0, row=1, pady=6, sticky="we")

# Modo: porcentaje o fijo
mode_var = tk.StringVar(value='pct')
mode_frame = ttk.Frame(frm)
mode_frame.grid(column=0, row=2, pady=(4, 8), sticky="we")
ttk.Radiobutton(mode_frame, text="Porcentaje", variable=mode_var, value='pct', command=actualizar).pack(side="left", padx=(0,8))
ttk.Radiobutton(mode_frame, text="Monto fijo", variable=mode_var, value='fixed', command=actualizar).pack(side="left")

# Porcentaje
ttk.Label(frm, text="Porcentaje (%)").grid(column=0, row=3, sticky="w")
pct_var = tk.StringVar(value="10")
pct_entry = ttk.Entry(frm, textvariable=pct_var, width=20)
pct_entry.grid(column=0, row=4, pady=6, sticky="we")

# Monto fijo
ttk.Label(frm, text="Propina fija (monto)").grid(column=0, row=5, sticky="w")
fixed_var = tk.StringVar(value="0.00")
fixed_entry = ttk.Entry(frm, textvariable=fixed_var, width=20)
fixed_entry.grid(column=0, row=6, pady=6, sticky="we")

# Personas
ttk.Label(frm, text="Dividir entre (personas)").grid(column=0, row=7, sticky="w")
people_var = tk.StringVar(value="1")
people_entry = ttk.Entry(frm, textvariable=people_var, width=20)
people_entry.grid(column=0, row=8, pady=6, sticky="we")

# Botones
btn_frame = ttk.Frame(frm)
btn_frame.grid(column=0, row=9, pady=10, sticky="we")
calc_btn = ttk.Button(btn_frame, text="Calcular", command=actualizar)
calc_btn.pack(side="left", padx=(0, 8))
reset_btn = ttk.Button(btn_frame, text="Limpiar", command=reset)
reset_btn.pack(side="left")

ttk.Separator(frm, orient="horizontal").grid(column=0, row=10, sticky="we", pady=8)

# Resultados
tip_var = tk.StringVar(value="—")
total_var = tk.StringVar(value="—")
per_var = tk.StringVar(value="—")
error_var = tk.StringVar(value="")

ttk.Label(frm, text="Propina:").grid(column=0, row=11, sticky="w")
ttk.Label(frm, textvariable=tip_var).grid(column=0, row=12, sticky="e")

ttk.Label(frm, text="Total:").grid(column=0, row=13, sticky="w")
ttk.Label(frm, textvariable=total_var).grid(column=0, row=14, sticky="e")

ttk.Label(frm, text="Por persona:").grid(column=0, row=15, sticky="w")
ttk.Label(frm, textvariable=per_var).grid(column=0, row=16, sticky="e")

error_label = ttk.Label(frm, textvariable=error_var, foreground="red")
error_label.grid(column=0, row=17, pady=(8, 0), sticky="we")

# Actualizar en tiempo real al cambiar entradas
for var in (bill_var, pct_var, fixed_var, people_var, mode_var):
    var.trace_add("write", actualizar)

root.columnconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
bill_entry.focus()
actualizar()

if __name__ == "__main__":
    root.mainloop()
