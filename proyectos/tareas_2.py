# ============================================================
# main.py — TODO JUNTO (punto de partida)
# ============================================================
# Una app de tareas con: añadir, completar, eliminar y listar.
# El problema: datos, lógica, validaciones y menú conviven.
# Imagina que esto tuviera 500 líneas... imposible de mantener.
# ============================================================

# ── DATOS ────────────────────────────────────────────────────
# Lista que almacena las tareas en memoria
tareas = []
contador_id = 1  # cada tarea tendrá un ID único


# ── VALIDACIONES ─────────────────────────────────────────────
def validar_descripcion(descripcion):
    """La descripción no puede estar vacía ni ser muy corta."""
    descripcion = descripcion.strip()
    if len(descripcion) < 3:
        return False, "La tarea debe tener al menos 3 caracteres."
    return True, descripcion

def validar_id(valor):
    """El ID debe ser un número entero positivo."""
    try:
        id_ = int(valor)
        if id_ <= 0:
            raise ValueError
        return True, id_
    except ValueError:
        return False, "El ID debe ser un número entero positivo."


# ── LÓGICA ───────────────────────────────────────────────────
def agregar_tarea(descripcion):
    global contador_id
    ok, resultado = validar_descripcion(descripcion)
    if not ok:
        return False, f"❌ {resultado}"
    tarea = {
        "id":          contador_id,
        "descripcion": resultado,
        "completada":  False,
    }
    tareas.append(tarea)
    contador_id += 1
    return True, f"✅ Tarea #{tarea['id']} añadida: '{resultado}'"

def completar_tarea(id_str):
    ok, resultado = validar_id(id_str)
    if not ok:
        return False, f"❌ {resultado}"
    for tarea in tareas:
        if tarea["id"] == resultado:
            if tarea["completada"]:
                return False, "⚠️  La tarea ya estaba completada."
            tarea["completada"] = True
            return True, f"✅ Tarea #{resultado} marcada como completada."
    return False, f"❌ No existe ninguna tarea con ID {resultado}."

def eliminar_tarea(id_str):
    ok, resultado = validar_id(id_str)
    if not ok:
        return False, f"❌ {resultado}"
    for i, tarea in enumerate(tareas):
        if tarea["id"] == resultado:
            tareas.pop(i)
            return True, f"🗑️  Tarea #{resultado} eliminada."
    return False, f"❌ No existe ninguna tarea con ID {resultado}."

def listar_tareas():
    if not tareas:
        print("  📭 No hay tareas todavía.")
        return
    print(f"\n  {'ID':<5} {'ESTADO':<12} DESCRIPCIÓN")
    print("  " + "─" * 40)
    for t in tareas:
        estado = "✅ Hecha  " if t["completada"] else "⏳ Pendiente"
        print(f"  {t['id']:<5} {estado:<12} {t['descripcion']}")
    print()


# ── MENÚ / UI ────────────────────────────────────────────────
def menu():
    # Datos de prueba
    agregar_tarea("Comprar leche")
    agregar_tarea("Estudiar Python")
    agregar_tarea("Hacer ejercicio")

    while True:
        print("\n╔══════════════════════════╗")
        print("║       TODO  LIST         ║")
        print("╠══════════════════════════╣")
        print("║ 1. Añadir tarea          ║")
        print("║ 2. Completar tarea       ║")
        print("║ 3. Eliminar tarea        ║")
        print("║ 4. Ver tareas            ║")
        print("║ 0. Salir                 ║")
        print("╚══════════════════════════╝")

        op = input("  Opción: ").strip()

        if op == "0":
            print("  👋 ¡Hasta luego!")
            break
        elif op == "1":
            desc    = input("  Descripción: ")
            _, msg  = agregar_tarea(desc)
            print(f"  {msg}")
        elif op == "2":
            id_str  = input("  ID de la tarea: ")
            _, msg  = completar_tarea(id_str)
            print(f"  {msg}")
        elif op == "3":
            id_str  = input("  ID a eliminar: ")
            _, msg  = eliminar_tarea(id_str)
            print(f"  {msg}")
        elif op == "4":
            listar_tareas()
        else:
            print("  ⚠️  Opción no válida.")

if __name__ == "__main__":
    menu()