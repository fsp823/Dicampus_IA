import re

def contar_vocales(texto: str) -> int:
    """
    Cuenta el número de vocales en una cadena de texto.

    La función detecta vocales tanto en mayúsculas como en minúsculas
    e incluye vocales con acento comunes en español (á, é, í, ó, ú, ü).

    Parámetros
    ----------
    texto : str
        Cadena de texto en la que se contarán las vocales.

    Retorna
    -------
    int
        Número total de vocales encontradas en el texto.
    """

    patron_vocales = r"[aeiouáéíóúüAEIOUÁÉÍÓÚÜ]"
    coincidencias = re.findall(patron_vocales, texto)
    return len(coincidencias)


if __name__ == "__main__":
    frase: str = input("Introduce una frase: ")
    total: int = contar_vocales(frase)
    print(f"La frase contiene {total} vocal(es).")