import unidecode

diccionarioEs = {}
for i in range(65,91):
	if i < 79:
		diccionarioEs[chr(i)] = (i-65)
	else:
		diccionarioEs['Ñ'] = 14
		diccionarioEs[chr(i)] = (i-64)

diccionarioAs = {}
for i in range(32,224):
	if i < 127:
		diccionarioAs[chr(i)] = (i-32)
	elif i > 127:
		diccionarioAs[chr(i)] = (i-32-1)

print(diccionarioAs)

modulo = int(input("Modulo 27 o 191: "))

if(modulo == 27):
	diccionario = diccionarioEs
else:
	diccionario = diccionarioAs

clave = input("Ingrese la clave : ")
clave = clave.upper()

archivo = open("textoLabRes.txt", 'r')
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
	valor = (diccionario[mensaje[i]] - diccionario[clave[i%len(clave)]]) % modulo
	if(i==0):
		print(valor)
	msg_encriptado += list(diccionario.keys())[list(diccionario.values()).index(valor)]

frecuencias = {}
for i in range(len(msg_encriptado)):
	if msg_encriptado[i] in frecuencias:
		frecuencias[msg_encriptado[i]] += 1
	else:
		frecuencias[msg_encriptado[i]] = 1

print(frecuencias)

f=open("textoLab.txt","w")
f.write(msg_encriptado)
f.close()