def capitalizar(texto):
    """
    Devuelve el texto con la primera letra de cada palabra en mayúscula.
    Si el texto está vacío, devuelve "Texto vacío".
    """
    if texto == "":
        return "Texto vacío"

    return texto.title()


if __name__ == "__main__":
    texto = input("Introduce un texto: ")
    resultado = capitalizar(texto)
    print(resultado)