def procesClave(clave):
	lis = [0]*len(clave)
	pos = [0]*(len(clave)+1)
	for i in range(len(clave)):
		x = 1
		for j in range(0,i):
			if(clave[j] <= clave[i]):
				x += 1
			else:
				lis[j] += 1
				pos[lis[j]] = j+1
		lis[i] = x
		pos[x] = i+1
	return pos, lis



clave = str(input("Clave: "))
#clave = "CONVENIENCE"
posClave, lisClave = procesClave(clave)

archivo = open("textEncript.txt", 'r')
mensaje = archivo.read()
archivo.close()

matrizMsg2 = mensaje.split(' ')
matrizMsg = []
for i in matrizMsg2:
	if(i != ""):
		matrizMsg.append(i)

row = len(matrizMsg[0])
col = len(clave)

matriz = [None] * row
for i in range(row):
    matriz[i] = ["0"] * col

for i in lisClave:
	s = matrizMsg[i-1]
	lenS = len(s)
	k = 0
	for j in range(row):
		if(posClave[j+1] >= posClave[i]):
			matriz[j][posClave[i]-1] = s[k]
			k += 1

		if(k >= lenS):
			break

msgDes = ""

for i in range(row):
	for j in range(col):
		if(matriz[i][j] == "0"):
			break
		else:
			msgDes += matriz[i][j]

print(msgDes)