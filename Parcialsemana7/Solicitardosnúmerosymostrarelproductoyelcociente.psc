Algoritmo Solicitardosnúmerosymostrarelproductoyelcociente
	
	definir numero1, numero2, cociente Como Real
	
	escribir "ingrese el primer numero"
	leer numero1
	
	escribir "ingrese el segundo numero"
	leer numero2
	
	producto <- numero1 * numero2
	
	si numero2 <> 0 entonces 
		cociente <- numero1 / numero2
		
		escribir "el producto es", producto
		escribir "el producto es", cociente
		
	SiNo
		Escribir "el producto es"
		escribir "nose puede dividir entre 0"
	FinSi
	
FinAlgoritmo
