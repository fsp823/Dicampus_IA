Documentación del Programa: Calculadora de Propinas
1. Descripción General

La Calculadora de Propinas es una aplicación sencilla desarrollada en Python utilizando la biblioteca gráfica Tkinter.
El programa permite al usuario introducir el importe de una factura y calcular automáticamente una propina equivalente al 10 % del total.

La aplicación muestra:

El importe de la factura.

La propina calculada (10 %).

El total a pagar (factura + propina).

2. Requisitos del Sistema
Software necesario

Python 3.x

Biblioteca Tkinter (normalmente incluida con Python)

Instalación

Verificar que Python está instalado:

python --version

Si Tkinter no está disponible:

Linux (ejemplo Ubuntu/Debian):

sudo apt-get install python3-tk


3. Ejecución

En el directorio raiz ejecutar:

python src/tip_gui_v4.py


4. Funcionamiento del Programa

El programa realiza los siguientes pasos:

El usuario introduce el importe de la factura.

Al presionar el botón Calcular, el sistema:

Calcula el 10 % de propina.

Suma la propina al total de la factura.

Se muestran:

Propina

Total a pagar

4. Fórmula utilizada

Propina:

𝑝
𝑟
𝑜
𝑝
𝑖
𝑛
𝑎
=
𝑓
𝑎
𝑐
𝑡
𝑢
𝑟
𝑎
×
0.10
propina=factura×0.10

Total a pagar:

𝑡
𝑜
𝑡
𝑎
𝑙
=
𝑓
𝑎
𝑐
𝑡
𝑢
𝑟
𝑎
+
𝑝
𝑟
𝑜
𝑝
𝑖
𝑛
𝑎
total=factura+propina
5. Interfaz Gráfica

La interfaz incluye los siguientes componentes:

Componente	Descripción
Label	Texto descriptivo para el usuario
Entry	Campo para introducir la factura
Button	Botón para calcular la propina
Label de resultado	Muestra propina y total