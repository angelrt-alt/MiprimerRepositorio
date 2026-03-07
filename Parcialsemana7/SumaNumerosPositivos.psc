Algoritmo SumaNumerosPositivos
		Definir numero, suma Como Entero
		suma <- 0
		
		Repetir
			Escribir "Ingrese un número: "
			Leer numero
			
			Si numero >= 0 Entonces
				suma <- suma + numumero
			FinSi
			
		Hasta Que numero < 0
		
		Escribir "La suma de los números positivos ingresados es: "
		
FinProceso
