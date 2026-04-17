def transformar_palabras(lista, opcion):
    resultado = []

    for palabra in lista:
        if opcion == 1:
            resultado.append(palabra.upper())
        elif opcion == 2:
            resultado.append(palabra[::-1])
        elif opcion == 3:
            resultado.append(len(palabra))
        else:
            return "Opción no válida"

    return resultado
