def transformar_y_contar(texto, opcion):
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto[::-1]
    elif opcion == 4:
        resultado = texto.replace(" ", "")
    else:
        resultado = texto

    return len(resultado)


print(transformar_y_contar("Hola Mundo", 1))
