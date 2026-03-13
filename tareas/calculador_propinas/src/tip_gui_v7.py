"""
Interfaz gráfica para la calculadora de propinas.

Proporciona una ventana Tkinter que permite introducir el importe de la factura,
elegir entre aplicar un porcentaje o un monto fijo de propina, indicar el número
de personas para dividir el total y ver los resultados formateados según la
configuración regional del sistema.

La GUI delega la lógica de cálculo y el formateo de moneda en las funciones
exportadas por `src.tip_cli` (por ejemplo `calcular_propina` y `format_currency_local`).
Captura y muestra errores de validación devueltos por dichas funciones.

Parameters
----------
None
    Este módulo define una aplicación de escritorio; no expone una API con
    parámetros posicionales. Las entradas se leen desde widgets Tkinter:
    - `bill_var` : StringVar con el importe de la factura.
    - `pct_var` : StringVar con el porcentaje de propina.
    - `fixed_var` : StringVar con el monto fijo de propina.
    - `people_var` : StringVar con el número de personas.
    - `mode_var` : StringVar que indica el modo ('pct' o 'fixed').

Functions
---------
actualizar(*args)
    Lee los valores de los widgets, llama a `calcular_propina` y actualiza las
    variables de resultado (`tip_var`, `total_var`, `per_var`). Maneja
    `ValueError` para mostrar mensajes de error al usuario.
reset()
    Restaura los valores por defecto en los campos de entrada y fuerza una
    actualización de la vista.

Returns
-------
None
    Ejecutar el módulo como script arranca el bucle principal de Tkinter
    (`root.mainloop()`), por lo que la función principal no devuelve valor.

Raises
------
ValueError
    Puede propagarse desde `calcular_propina` si las entradas no son válidas.
Exception
    Errores inesperados en la UI se capturan y se muestran como mensaje de error,
    pero no se relanzan al usuario final.

Examples
--------
Ejecutar la aplicación desde la raíz del proyecto:

>>> python tip_gui.py

Uso típico desde la interfaz:
- Introducir "100" en Valor de la factura.
- Seleccionar "Porcentaje" y dejar 10 en Porcentaje (%) → pulsar Calcular.
- Ver "Propina", "Total" y "Por persona" formateados según la locale.

Notes
-----
- La GUI intenta importar `calcular_propina` y `format_currency_local` desde
  `src.tip_cli`. Si el import falla, añade la raíz del proyecto a `sys.path`
  para facilitar el desarrollo local.
- El formateo de moneda usa `babel` si está disponible; si no, recurre a
  `locale` y a un fallback seguro.
- Las entradas aceptan cadenas con coma decimal (por ejemplo "12,34") porque
  la conversión y validación se realizan en `src.tip_cli`.
- `locale.setlocale` puede cambiar el locale global del proceso; para evitar
  efectos en aplicaciones multihilo, instale `Babel` y el formateo no tocará
  el estado global.

See Also
--------
src.tip_cli.calcular_propina : Lógica de cálculo y validación de entradas.
src.tip_cli.format_currency_local : Formateo de importes según locale.

Todo
----
- Añadir atajos de teclado (Enter = Calcular, Esc = Limpiar).
- Añadir selector manual de moneda además de la detección automática.
"""

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

def reset(*_):
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

# Atajos de teclado: Enter = Calcular, Esc = Limpiar
# Se enlazan al root para que funcionen desde cualquier widget
root.bind('<Return>', lambda event: actualizar())
root.bind('<KP_Enter>', lambda event: actualizar())  # Enter del teclado numérico
root.bind('<Escape>', lambda event: reset())

# Ajustes de ventana y foco
root.columnconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
bill_entry.focus()
actualizar()

if __name__ == "__main__":
    root.mainloop()
