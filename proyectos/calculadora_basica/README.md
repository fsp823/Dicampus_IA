# Calculadora de Números Naturales en Python

Aplicación de consola escrita en Python que permite realizar operaciones básicas (suma, resta, multiplicación y división) utilizando únicamente números naturales.  
Incluye un menú repetitivo que facilita la interacción con el usuario hasta que este decide salir.
Incluye también un archivo de pruebas unitarias.

**Autor:** Fernando Sirgado Polo

---

## Características

- Operaciones disponibles:
  - Suma
  - Resta
  - Multiplicación
  - División (con control de división entre cero)
- Validación para asegurar que solo se introducen números naturales (enteros mayores o iguales que 0)
- Menú interactivo que se repite hasta que el usuario elige salir
- Funciones separadas para cada operación, lo que mejora la claridad y el mantenimiento del código

---

## Requisitos

- Python 3.x instalado en el sistema

---

## Cómo ejecutar la aplicación

1. Descarga o copia el archivo `.py` que contiene el código de la calculadora.
2. Abre una terminal o consola.
3. Ejecuta el programa con:

```bash
python app.py


##  Documentación de Funciones

###  `sumar(a, b)`
**Descripción**: Calcula la suma de dos números.  
**Parámetros**: 
- `a`: Primer número (entero)
- `b`: Segundo número (entero)  
**Retorno**: Resultado de `a + b`  
**Ejemplo**: `sumar(5, 3)` → `8`

### ➖ `restar(a, b)`
**Descripción**: Calcula la resta de dos números.  
**Parámetros**:
- `a`: Primer número (entero)
- `b`: Segundo número (entero)
**Retorno**: Resultado de `a - b`
**Ejemplo**: `restar(10, 4)` → `6`

### ✖️ `multiplicar(a, b)`
**Descripción**: Calcula la multiplicación de dos números.  
**Parámetros**:
- `a`: Primer número (entero)
- `b`: Segundo número (entero)
**Retorno**: Resultado de `a * b`
**Ejemplo**: `multiplicar(6, 7)` → `42`

### ➗ `dividir(a, b)`
**Descripción**: Calcula la división de dos números.  
**Parámetros**:
- `a`: Dividendo (entero)
- `b`: Divisor (entero)
**Retorno**: Resultado de `a / b`
**Excepción**: Lanza `ValueError` si `b` es cero
**Ejemplo**: `dividir(10, 2)` → `5`

### 🖥️ Funciones de interfaz
- **`Bucle(while True)`**: Muestra por pantalla las opciones disponibles (1: Sumar, 2: Restar, 3: Multiplicar, 4: Dividir, 5: Salir y controla el flujo principal del programa, pide los números al usuario y muestra los resultados)

---

## 🧪 Sistema de Pruebas

### 📋 ¿Qué verifican las pruebas?

✔️ Suma (test_sumar)
Verifica que la función suma correctamente dos números naturales.

Comprueba casos básicos como:

3 + 5 = 8

0 + 0 = 0

✔️ Resta (test_restar)
Comprueba que la resta funciona correctamente.

Evalúa:

10 − 4 = 6

5 − 5 = 0

✔️ Multiplicación (test_multiplicar)
Asegura que la multiplicación devuelve el resultado esperado.

Casos incluidos:

3 × 4 = 12
0 × 7 = 0

✔️ División (test_dividir)
Verifica divisiones válidas:

10 / 2 = 5

9 / 3 = 3

Comprueba el manejo de errores:

División entre cero devuelve el mensaje:
"Error: no se puede dividir entre cero."

Cómo ejecutar las pruebas
Asegúrate de que los archivos app.py y test_calculadora.py están en la misma carpeta.

Abre una terminal en esa ubicación.

Ejecuta:

bash
python -m unittest test.py
Para ejecutar todas las pruebas del directorio:

bash
python -m unittest
Objetivo de las pruebas
Estas pruebas garantizan que:

Las operaciones matemáticas funcionan correctamente.

El programa maneja adecuadamente casos límite.

La división entre cero no provoca errores y devuelve un mensaje controlado.

El comportamiento del programa es estable y predecible.

---
