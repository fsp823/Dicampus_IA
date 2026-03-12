# Tarea: Modularización de aplicaciones en Python

**Objetivo**  
Aprender a organizar código Python separando responsabilidades en diferentes archivos y carpetas (principios básicos de **Clean Code** y **arquitectura modular**).

**Fecha límite sugerida:** [12/03/2026]  
**Entrega:** Carpeta con tu nombre o repo a   ( GitHub)

## Parte 1 – Aplicación de Lista de Tareas (TODO List)

**Código inicial (todo junto):** `main.py` (versión monolítica)

**Tarea:**  
Reorganizar el código en **al menos** estos archivos:


**Requisitos mínimos:**

- `main.py` **no debe** contener lógica de tareas ni validaciones
- Debes usar `import` correctamente (puedes usar `from xxx import yyy`)
- Mantener la funcionalidad exactamente igual (incluyendo los mensajes con emojis)
- (Opcional pero muy recomendado) Usar `if __name__ == "__main__":`

## Parte 2 – Aplicación de Biblioteca / Librería

**Código inicial (todo junto):** el segundo archivo grande

**Tarea:**  
Reorganizar en **al menos** estas partes:


**Requisitos mínimos:**

- La clase `Libro` debe estar en un archivo separado (`models.py` recomendado)
- Toda la lógica de la biblioteca (agregar, prestar, devolver, vender, comprar, mostrar) debe estar en `biblioteca.py`
- `main.py` solo debe:

  - crear la instancia de `Biblioteca`
  - cargar datos de prueba (si los quieres mantener)
  - mostrar el menú y llamar a los métodos

**Opcional (muy valorado):**

- Crear un archivo `datos_prueba.py` con una función que devuelva libros de ejemplo
- Usar **type hints** en las funciones y métodos
- Agregar **docstrings** cortos en las funciones principales




## Criterios de evaluación (aproximados)

- Separación clara de responsabilidades (5 pts)
- Correcto uso de `import` sin errores (4 pts)
- El programa funciona igual que el original (4 pts)
- `main.py` limpio y legible (3 pts)
- Uso de buenas prácticas (nombres claros, type hints, docstrings) (+2–4 pts extra)
- Estructura de carpetas lógica y ordenada (+2 pts extra)

¡Éxito!  
Cualquier duda sobre cómo importar entre archivos o estructurar mejor, preguntar en clase o por el canal correspondiente.

Última actualización: febrero 2026