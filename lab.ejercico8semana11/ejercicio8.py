def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto[::-1]
    else:
        return "Opción no válida"


def main():
    texto = input("Ingrese un texto: ")

    print("\nSeleccione una opción:")
    print("1. Convertir a MAYÚSCULAS")
    print("2. Convertir a minúsculas")
    print("3. Invertir texto")

    try:
        opcion = int(input("Ingrese opción (1, 2 o 3): "))
        resultado = transformar_texto(texto, opcion)
        print("\nResultado:", resultado)
    except ValueError:
        print("Debe ingresar un número válido.")


if __name__ == "__main__":
    main()