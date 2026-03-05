def validar_email(email):
    """
    Comprueba si un email contiene '@' y '.'.
    Devuelve True si cumple ambas condiciones, False en caso contrario.
    """
    if "@" in email and "." in email:
        return True
    return False


if __name__ == "__main__":
    email = input("Introduce un email: ")
    if validar_email(email):
        print("Email válido")
    else:
        print("Email no válido")