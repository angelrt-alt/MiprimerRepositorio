Algoritmo ejemplo2
	Definir cajero, cuentadeahorro, numerodecuenta, cantidadsaliente, saldo, preguntar Como Entero
	cuentadeahorro = 1000
	numerodecuenta = 12345
	
	Escribir " bienvenido"
	Escribir "actividad que desea realizar"
	Escribir "1 para consultar"
	Escribir "2 para extraer dinero de la cuenta de ahorro"
	
	Escribir "escriba el numro de cuenta a operar"
	leer preguntar // yo no quiero ser un uno mejor busco otra chamba
	
	si preguntar == 1
		Escribir "escriba el numro de cuenta a operar"
		leer preguntar // es valor de numero de cuentas
		
		si preguntar == numerodecuenta
			escribir "su saldo es" cuentadeahorro
		FinSi
	FinSi
	
	si preguntar == 2
		Escribir "escriba el numero de cueta a operar"
		leer preguntar // es valor den numero de cuentas
		si preguntar == numerodecuenta
			Escribir "escriba el monto a extraer"
			leer preguntar // es la cantidad a extraer
			
			si preguntar <= cuentadeahorro
				saldo = cuentadeahorro - preguntar
				Escribir  "procesando"
				escribir "su saldo actual es de", saldo 
			FinSi
			
		FinSi
	FinSi
	//or o pues llevar
	//panes con cafe o chocolate
	
	//and puedes llevar carne y jamon
	
		// not mejor no
	
		// ==si es igual
		// <> diferente <>
	//no pueden comenzar con
	//numero
	//signos a menos que sea_
	//no teben llevar espacio
	//si es una calse siempre incia con Mayuscula
	// es evitar el codigo espagueti
FinAlgoritmo
