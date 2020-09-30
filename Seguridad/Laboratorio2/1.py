import unidecode

diccionario = {}
for i in range(65,91):
	if i < 79:
		diccionario[chr(i)] = (i-65)
	else:
		diccionario['Ñ'] = 14
		diccionario[chr(i)] = (i-64)

modulo = int(input("Modulo 27 o 191: "))
clave = input("Ingrese la clave : ")
clave = clave.upper()

archivo = open("textoLab.txt", 'r')
mensaje = archivo.read()

mensaje = mensaje.strip()
mensaje = mensaje.replace(" ","")
mensaje = unidecode.unidecode(mensaje)
mensaje = mensaje.upper()

mensaje2 = ""
for i in range(len(mensaje)):
	if(mensaje[i] in diccionario):
		mensaje2 += mensaje[i]

mensaje = mensaje2

msg_encriptado = ""

for i in range(len(mensaje)):
	valor = (diccionario[mensaje[i]] + diccionario[clave[i%len(clave)]]) % modulo
	msg_encriptado += list(diccionario.keys())[list(diccionario.values()).index(valor)]

print(msg_encriptado)