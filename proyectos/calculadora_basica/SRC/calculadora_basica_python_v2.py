def main():
    while True:
        print("\n--- Calculadora de números naturales ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        n = (0)
        opcion = input("Elige una opción: ")
        mensaje =input("Escribe un número natural: ")

        if opcion == "5":
            print("Saliendo de la calculadora...")
            break

        def pedir_natural(mensaje):
            n = int(input(mensaje))
        while n < 0:
            print("Error: introduce un número natural (0 o mayor).")
            n = int(input(mensaje))
        return n


        a = pedir_natural("Introduce el primer número: ")
        b = pedir_natural("Introduce el segundo número: ")

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
