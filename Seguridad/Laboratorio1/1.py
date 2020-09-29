import unidecode

archivo = open("texto.txt", 'r')
mensaje = archivo.read()

tamaño = len(mensaje)

mensaje = unidecode.unidecode(mensaje)

correccion = ""

for i in range(tamaño):
	if(mensaje[i] == 'j' or mensaje[i] == 'h'):
		correccion = correccion + 'i'
	elif(mensaje[i] == 'ñ'):
		correccion = correccion + 'n'
	elif(mensaje[i] == 'k'):
		correccion = correccion + 'l'
	elif(mensaje[i] == 'u' or mensaje[i] == 'w'):
		correccion = correccion + 'v'
	elif(mensaje[i] == 'y'):
		correccion = correccion + 'z'
	elif(mensaje[i] != ',' and mensaje[i] != ';' 
		and mensaje[i] != '.' and mensaje[i] != '!' 
		and mensaje[i] != ' ' and mensaje[i] != '\n'):
			correccion = correccion + mensaje[i]

correccion = correccion.upper()

f=open("HERALDOSNEGROS_pre.txt","w")
f.write(correccion)
f.close()
