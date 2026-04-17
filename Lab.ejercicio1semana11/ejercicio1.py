def transformar_mayusculas(texto, numero):
    if numero == 1:
        return texto.upper()
    else:
        return "Número no válido"


print(transformar_mayusculas("hola mundo", 1))  # HOLA MUNDO