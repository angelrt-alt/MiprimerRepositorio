def transformar_texto(texto, operaciones):
    for op in operaciones:
        if op == 1:
            texto = texto.upper()
        elif op == 2:
            texto = texto[::-1]
        elif op == 3:
            texto = texto.replace(" ", "")
    return texto
    resultado = transformar_texto("Hola mundo", [1, 2, 3])
