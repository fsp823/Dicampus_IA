def convertir_celsius(grados: float) -> float:
    """Convierte grados Celsius a Fahrenheit.
    
    Args:
        grados (float): Temperatura en Celsius.
    Returns:
        float: Temperatura equivalente en Fahrenheit.
    
    Ejemplos:
        >>> convertir_celsius(0)    # 32.0
        >>> convertir_celsius(100)  # 212.0
    """
    return (grados * 9/5) + 32

# Pruebas
print(convertir_celsius(0))    # Esperado: 32.0
print(convertir_celsius(100))  # Esperado: 212.0
print(convertir_celsius(37))   # Temperatura corporal
print(convertir_celsius(-40))  # Caso especial: -40 C = -40 F


def filtrar_pares(numeros: list) -> list:
    """Devuelve solo los números pares de una lista.
    
    Args:
        numeros (list): Lista de números enteros.
    Returns:
        list: Lista con solo los números pares.
    
    Ejemplos:
        >>> filtrar_pares([1, 2, 3, 4, 5, 6])  # [2, 4, 6]
        >>> filtrar_pares([1, 3, 5])            # []
    """
    return [n for n in numeros if n % 2 == 0]

# Pruebas filtrar_pares
print(filtrar_pares([1, 2, 3, 4, 5, 6]))  # Esperado: [2, 4, 6]
print(filtrar_pares([10, 15, 20, 25]))     # Tu prediccion: [10, 20]
print(filtrar_pares([]))                   # Tu prediccion: error
print(filtrar_pares([7, 11, 13]))          # Tu prediccion: [0]