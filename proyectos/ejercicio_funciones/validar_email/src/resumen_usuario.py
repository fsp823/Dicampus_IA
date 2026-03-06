from validar_email import validar_email


def resumen_usuario(nombre, email):
    """
    Capitaliza el nombre del usuario y valida el email.
    Devuelve un mensaje indicando si el email es correcto o no.
    """

    nombre_capitalizado = nombre.title()

    if validar_email(email):
        return f"Usuario: {nombre_capitalizado} - Email correcto"
    else:
        return f"Usuario: {nombre_capitalizado} - Email inválido"


if __name__ == "__main__":
    nombre = input("Introduce el nombre del usuario: ")
    email = input("Introduce el email del usuario: ")

    print(resumen_usuario(nombre, email))