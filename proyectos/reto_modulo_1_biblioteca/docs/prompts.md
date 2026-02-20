Talento Solutions. Quieren probar
cómo la IA puede ayudar a programar un sistema sencillo de gestión de
biblioteca: libros, préstamos, devoluciones, etc.

Hazme el proyecto en python con esta estructura: 
o src/biblioteca.py (o similar)
o tests/test_biblioteca.py
o docs/proceso_ia.md
o README.md
o .gitignore
o requirements.txt (si lo necesitas)

no. genera 5 historias de usuario para un sistema de biblioteca, y genera también un diagrama de flujo (en texto) del proceso de préstamo.

no. genérame en biblioteca.py un menú de consola para acceder a las funciones e introducir los datos.

no, ahora genérame 5 test unitarios en un archivo llamado test_biblioteca.py

hazme pruebas unitarias incluyendo el menú de consola

estoy intentando ejecutar las pruebas con este comando python -m test_biblioteca_v3.py y me sale este error:  
Traceback (most recent call last):
  File "<frozen runpy>", line 189, in _run_module_as_main
  File "<frozen runpy>", line 112, in _get_module_details
  File "C:\GitHub\Dicampus_IA\proyectos\reto_modulo_1_biblioteca\tests\test_biblioteca_v3.py", line 2, in <module>
    from src.biblioteca_v2 import Biblioteca, Libro, Usuario
ModuleNotFoundError: No module named 'src'

en las pruebas unitarias me indica que falta una función main en biblioteca.py, refactoriza el código de este archivo y añádela.

hazme un archivo de pruebas unitarias para este último código

me aparece este error: ImportError while importing test module 'C:\GitHub\Dicampus_IA\proyectos\reto_modulo_1_biblioteca\tests\test_biblioteca_v3.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests\test_biblioteca_v3.py:2: in <module>
    from src.biblioteca_v3 import biblioteca
E   ImportError: cannot import name 'biblioteca' from 'src.biblioteca_v3' (C:\GitHub\Dicampus_IA\proyectos\reto_modulo_1_biblioteca\src\biblioteca_v3.py)


acabo de utilizar la solución 1 y me sale este error: FAILED tests/test_biblioteca_v3.py::test_menu_agregar_libro - TypeError: main() missing 1 required positional argument: 'biblioteca' FAILED tests/test_biblioteca_v3.py::test_menu_prestar_libro - TypeError: main() missing 1 required positional argument: 'biblioteca' FAILED tests/test_biblioteca_v3.py::test_menu_opcion_invalida - TypeError: main() missing 1 required positional argument: 'biblioteca'


qué tareas harías con automatización “normal” (scripts, GitHub Actions) y qué tareas mejorarías con IA


no. Hazme una revisión del código y dime de donde lo has sacado


revisa el código de biblioteca.py buscando fallas de seguridad

si

no. ¿Puedes hacer una imagen que englobe toda nuestra coversación?
