import unidecode

diccionario = {}
for i in range(65,91):
    diccionario[chr(i)] = (i-65)

# print(diccionarioAs)

modulo = 26

clave = int(input("Ingrese la clave : "))
clave = chr(clave+65)

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

opcion = input("cifrar o descifrar: ")
if opcion == "cifrar":
	opcion = 1
elif opcion == "descifrar":
	opcion = -1

for i in range(len(mensaje)):
	valor = (diccionario[mensaje[i]] + opcion * diccionario[clave[i%len(clave)]]) % modulo
	msg_encriptado += list(diccionario.keys())[list(diccionario.values()).index(valor)]

print(msg_encriptado)

frecuencias = {}
for i in range(len(msg_encriptado)):
	if msg_encriptado[i] in frecuencias:
		frecuencias[msg_encriptado[i]] += 1
	else:
		frecuencias[msg_encriptado[i]] = 1

# print(frecuencias)

f=open("textoLabRes.txt","w")
f.write(msg_encriptado)
f.close()