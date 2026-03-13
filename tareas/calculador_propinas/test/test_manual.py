# test_manual.py
from src.tip_cli import calcular_propina

# casos de prueba
assert calcular_propina(0.0, 10.0) == (0.0, 0.0)
assert calcular_propina(100.0, 10.0) == (10.0, 110.0)
assert calcular_propina(42.5, 10.0) == (4.25, 46.75)

print("Todos los asserts pasaron.")
