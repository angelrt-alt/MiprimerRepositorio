def procesar_texto(texto, numero):
    if numero not in [1, 2, 3]:
        return "Opción inválida"

    if numero == 1:
        return texto.upper()  # convierte a mayúsculas
    elif numero == 2:
        return texto.lower()  # convierte a minúsculas
    elif numero == 3:
        return texto[::-1]  # invierte el texto
