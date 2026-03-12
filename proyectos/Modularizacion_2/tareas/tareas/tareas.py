# tareas.py

import datos.datos as datos
from validaciones.validaciones import validar_descripcion, validar_id


def agregar_tarea(descripcion):
    ok, resultado = validar_descripcion(descripcion)

    if not ok:
        return False, f"❌ {resultado}"

    tarea = {
        "id": datos.contador_id,
        "descripcion": resultado,
        "completada": False,
    }

    datos.tareas.append(tarea)
    datos.contador_id += 1

    return True, f"✅ Tarea #{tarea['id']} añadida: '{resultado}'"


def completar_tarea(id_str):
    ok, resultado = validar_id(id_str)

    if not ok:
        return False, f"❌ {resultado}"

    for tarea in datos.tareas:
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

    for i, tarea in enumerate(datos.tareas):
        if tarea["id"] == resultado:
            datos.tareas.pop(i)
            return True, f"🗑️  Tarea #{resultado} eliminada."

    return False, f"❌ No existe ninguna tarea con ID {resultado}."


def listar_tareas():
    if not datos.tareas:
        print("  📭 No hay tareas todavía.")
        return

    print(f"\n  {'ID':<5} {'ESTADO':<12} DESCRIPCIÓN")
    print("  " + "─" * 40)

    for t in datos.tareas:
        estado = "✅ Hecha  " if t["completada"] else "⏳ Pendiente"
        print(f"  {t['id']:<5} {estado:<12} {t['descripcion']}")

    print()