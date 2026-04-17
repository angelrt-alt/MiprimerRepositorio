def transformar(texto, numero, opcion):
    if opcion == 1:
        return texto.upper() * numero
    elif opcion == 2:
        return texto.lower() * numero
    elif opcion == 3:
        return texto[::-1] * numero
    else:
        return "Opción no válida"


# Solicitar datos al usuario
texto = input("Ingrese un texto: ")
numero = int(input("Ingrese un número: "))

print("Opciones:")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Invertir texto")

opcion = int(input("Elija una opción: "))

# Llamar a la función
resultado = transformar(texto, numero, opcion)

print("Resultado:", resultado)
