def transformar_palabra(palabra, opcion):
    if opcion == 1:
        resultado = palabra.upper()
    elif opcion == 2:
        resultado = palabra.lower()
    elif opcion == 3:
        resultado = palabra[::-1]
    else:
        resultado = "Opción no válida"

    print(resultado)


# Ejemplos
transformar_palabra("Hola", 1)  # HOLA
transformar_palabra("Hola", 2)  # hola
transformar_palabra("Hola", 3)  # aloH
