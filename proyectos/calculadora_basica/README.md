Calculadora de Números Naturales en Python
Aplicación de consola escrita en Python que permite realizar operaciones básicas (suma, resta, multiplicación y división) utilizando únicamente números naturales. Incluye un menú repetitivo que facilita la interacción con el usuario hasta que este decide salir.



Fernando Sirgado Polo

Características
Operaciones disponibles:

Suma

Resta

Multiplicación

División (con control de división entre cero)

Validación para asegurar que solo se introducen números naturales (enteros mayores o iguales que 0)

Menú interactivo que se repite hasta que el usuario elige salir

Funciones separadas para cada operación, lo que mejora la claridad y el mantenimiento del código

Requisitos
Python 3.x instalado en el sistema

Cómo ejecutar la aplicación
Descarga o copia el archivo .py que contiene el código de la calculadora.

Abre una terminal o consola.

Ejecuta el programa con:

Código
python app.py
Sigue las instrucciones del menú para realizar operaciones.

Funcionamiento del menú
Al iniciar el programa, se mostrará un menú como este:

Código
--- Calculadora de números naturales ---
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
El usuario debe introducir el número de la opción deseada.
Después, el programa pedirá dos números naturales y mostrará el resultado de la operación seleccionada.

El menú se repetirá automáticamente hasta que el usuario elija la opción 5. Salir.

Estructura del código
Funciones de operaciones: sumar, restar, multiplicar, dividir

Función auxiliar: pedir_natural() para validar que el usuario introduce números naturales

Bucle principal: gestiona el menú y las opciones del usuario

Ejemplo de uso:
Código
--- Calculadora de números naturales ---
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Elige una opción: 1
Introduce el primer número: 7
Introduce el segundo número: 5
Resultado: 12


Pruebas unitarias
El proyecto incluye un archivo de pruebas unitarias (por ejemplo, test.py) que verifica el correcto funcionamiento de las funciones principales de la calculadora: sumar, restar, multiplicar y dividir.

Las pruebas están implementadas con el módulo estándar unittest de Python.

Cómo ejecutar las pruebas
Asegúrate de que el archivo calculadora.py y el archivo de pruebas test_calculadora.py están en la misma carpeta.

Abre una terminal en esa carpeta.

Ejecuta:

Código
python -m unittest test_calculadora.py
También puedes ejecutar todas las pruebas del directorio con:

Código
python -m unittest
Qué comprueban las pruebas
Que cada operación devuelve el resultado esperado.

Que la división entre cero devuelve el mensaje de error correspondiente.

Que las funciones se comportan correctamente con números naturales y casos límite.

Ejemplo de archivo de pruebas
python
import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 5), 8)
        self.assertEqual(sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 4), 6)
        self.assertEqual(restar(5, 5), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(0, 7), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 0), "Error: no se puede dividir entre cero.")

if __name__ == "__main__":
    unittest.main()


Licencia
Este proyecto puede utilizarse libremente con fines educativos o personales.