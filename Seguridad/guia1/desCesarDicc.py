import json

data = {}
with open('refer.json') as file:
    data = json.load(file)

archivo = open("textoLabRes.txt", 'r')
mensajeEn = archivo.read()

diccionario = {}
for i in range(65,91):
    diccionario[chr(i)] = (i-65)

flag = False
flag2 = False
key = 0

for k in range(0, 26):
    for msg in data:
        msgEn = data[msg]
        for i in range(len(msg)):
            if (diccionario[msg[i]] + k) % 26 != diccionario[msgEn[i]]:
                flag = True
                break
            elif i == len(msg) - 1:
                flag2 = True
        if flag:
            flag2 = False
            break
    if flag:
        flag = False
        flag2 = False
        continue
    elif flag2:
        key = k
        break

clave = chr(key+65)
msg_desencriptado = ""

for i in range(len(mensajeEn)):
	valor = (diccionario[mensajeEn[i]] - diccionario[clave[i%len(clave)]]) % 26
	msg_desencriptado += list(diccionario.keys())[list(diccionario.values()).index(valor)]

print(msg_desencriptado)
print("Clave:", key)
f=open("textoLab.txt","w")
f.write(msg_desencriptado)
f.close()