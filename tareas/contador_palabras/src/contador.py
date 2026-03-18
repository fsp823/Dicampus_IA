"""
contador.py
Funciones para contar palabras y calcular frecuencias en un texto
o en archivos de texto.
"""

import re
from collections import Counter
from pathlib import Path


# -----------------------------
# Limpieza y procesamiento
# -----------------------------

def limpiar_texto(texto: str) -> str:
    """
    Normaliza el texto:
    - Convierte a minúsculas
    - Elimina signos de puntuación
    - Reemplaza saltos de línea por espacios
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser una cadena de caracteres")

    texto = texto.lower()
    texto = texto.replace("\n", " ")

    # Eliminar caracteres no alfanuméricos (excepto espacios)
    texto = re.sub(r"[^a-záéíóúüñ0-9 ]", "", texto)

    return texto


def obtener_palabras(texto: str) -> list:
    """
    Convierte el texto en una lista de palabras limpias.
    """
    texto_limpio = limpiar_texto(texto)
    return texto_limpio.split()


# -----------------------------
# Funciones principales
# -----------------------------

def contar_palabras(texto: str) -> int:
    """
    Devuelve el número total de palabras en el texto.
    """
    return len(obtener_palabras(texto))


def frecuencia_palabras(texto: str) -> dict:
    """
    Devuelve un diccionario con la frecuencia de cada palabra.
    """
    palabras = obtener_palabras(texto)
    return dict(Counter(palabras))


def top_palabras(texto: str, n: int = 5) -> list:
    """
    Devuelve una lista con las n palabras más frecuentes.
    """
    if n <= 0:
        raise ValueError("El número de palabras debe ser mayor que cero")

    frecuencias = frecuencia_palabras(texto)
    return Counter(frecuencias).most_common(n)


# -----------------------------
# Lectura de archivos
# -----------------------------

def leer_archivo(ruta: str | Path) -> str:
    """
    Lee un archivo de texto y devuelve su contenido como cadena.
    """
    ruta = Path(ruta)

    if not ruta.exists():
        raise FileNotFoundError(f"El archivo no existe: {ruta}")

    if not ruta.is_file():
        raise ValueError(f"La ruta no es un archivo válido: {ruta}")

    with ruta.open("r", encoding="utf-8") as f:
        return f.read()


def analizar_archivo(ruta: str | Path) -> dict:
    """
    Analiza un archivo de texto y devuelve:
    - total de palabras
    - frecuencias
    - top 5 palabras
    """
    contenido = leer_archivo(ruta)

    return {
        "total_palabras": contar_palabras(contenido),
        "frecuencias": frecuencia_palabras(contenido),
        "top_5": top_palabras(contenido, 5)
    }


# -----------------------------
# Ejecución directa
# -----------------------------

if __name__ == "__main__":
    archivo = "textos/ejemplo.txt"
    print(f"Analizando archivo: {archivo}")

    resultado = analizar_archivo(archivo)

    print("Total de palabras:", resultado["total_palabras"])
    print("Top 5 palabras:", resultado["top_5"])
