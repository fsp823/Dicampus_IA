"""
main.py
Script para ejecutar el contador de palabras desde la terminal.
Permite:
- Analizar un archivo con --archivo
- Leer texto largo desde stdin (pipes o redirecciones)
"""

import argparse
import sys
from src.contador import analizar_archivo, contar_palabras, frecuencia_palabras, top_palabras


def leer_stdin() -> str:
    """
    Lee texto desde la entrada estándar si hay contenido.
    Devuelve una cadena vacía si no hay nada.
    """
    if sys.stdin.isatty():
        # No hay datos en stdin (el usuario no ha hecho pipe ni redirección)
        return ""
    return sys.stdin.read()


def main():
    parser = argparse.ArgumentParser(
        description="Contador de palabras en archivos o texto desde stdin"
    )

    parser.add_argument(
        "--archivo",
        type=str,
        help="Ruta del archivo de texto a analizar"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Número de palabras más frecuentes a mostrar (por defecto 5)"
    )

    args = parser.parse_args()

    # 1. Intentar leer desde stdin
    texto_stdin = leer_stdin()

    # 2. Si hay texto en stdin, lo analizamos
    if texto_stdin.strip():
        print("\n📄 Analizando texto recibido por stdin...\n")
        total = contar_palabras(texto_stdin)
        frec = frecuencia_palabras(texto_stdin)
        top = top_palabras(texto_stdin, args.top)

        print(f"Total de palabras: {total}")
        print(f"\nTop {args.top} palabras más frecuentes:")
        for palabra, freq in top:
            print(f"  - {palabra}: {freq}")
        return

    # 3. Si no hay stdin, pero sí archivo
    if args.archivo:
        try:
            resultado = analizar_archivo(args.archivo)
        except Exception as e:
            print(f"Error: {e}")
            return

        print("\n📄 RESULTADOS DEL ANÁLISIS")
        print("---------------------------")
        print(f"Archivo analizado: {args.archivo}")
        print(f"Total de palabras: {resultado['total_palabras']}")
        print(f"\nTop {args.top} palabras más frecuentes:")

        for palabra, frecuencia in resultado["top_5"][:args.top]:
            print(f"  - {palabra}: {frecuencia}")
        return

    # 4. Si no hay ni archivo ni stdin, mostrar ayuda
    print("No se proporcionó texto. Usa:")
    print("  python main.py --archivo textos/ejemplo.txt")
    print("  cat archivo.txt | python main.py")
    print("  python main.py < archivo.txt")


if __name__ == "__main__":
    main()
