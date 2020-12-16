import unidecode
import operator

archivo = open("textoLabRes.txt", 'r')
mensaje = archivo.read()
mensaje = unidecode.unidecode(mensaje)
mensaje = mensaje.strip()
mensaje = mensaje.replace(" ","")
mensaje = mensaje.replace("\n","")
mensaje = mensaje.upper()
archivo.close()
mensajeEncriptado = mensaje
total = len(mensaje)
dicEncrypt = {}
for ch in mensaje:
    if ch in dicEncrypt:
        dicEncrypt[ch] += 1
    else:
        dicEncrypt[ch] = 1
for k in dicEncrypt:
    dicEncrypt[k] = (dicEncrypt[k]*100)/total

dicPlain = {}
total = 0
for i in range(1,4):
    nameFile = f'text{i}.txt'
    archivo = open(nameFile, 'r')
    mensaje = archivo.read()
    mensaje = unidecode.unidecode(mensaje)
    mensaje = mensaje.strip()
    mensaje = mensaje.replace(" ","")
    mensaje = mensaje.replace("\n","")
    mensaje = mensaje.upper()
    archivo.close()
    total += len(mensaje)
    for ch in mensaje:
        if ch in dicPlain:
            dicPlain[ch] += 1
        else:
            dicPlain[ch] = 1

for k in dicPlain:
    dicPlain[k] = (dicPlain[k]*100)/total

dicPlain_sort = sorted(dicPlain.items(), key=operator.itemgetter(1), reverse=True)
dicEncrypt_sort = sorted(dicEncrypt.items(), key=operator.itemgetter(1), reverse=True)

mostPopularPlain = dicPlain_sort[0][0]
mostPopularEncrypt = dicEncrypt_sort[0][0]

diccionario = {}
for i in range(65,91):
    diccionario[chr(i)] = (i-65)

mensajeDes = ""
clave = 0
for i in range(0,26):
    if (diccionario[mostPopularPlain] + i) % 26 == diccionario[mostPopularEncrypt]:
        clave = chr(i+65)
        for i in range(len(mensajeEncriptado)):
            valor = (diccionario[mensajeEncriptado[i]] - diccionario[clave[i%len(clave)]]) % 26
            mensajeDes += list(diccionario.keys())[list(diccionario.values()).index(valor)]
        print('Key = %s: %s' % (clave, mensajeDes))
        break