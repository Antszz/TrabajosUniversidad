def kasiski(texto):
	frecuencias = {}
	for i in range(0,len(texto)):
		triada = texto[i:i+3]
		if(len(triada)<3):
			break
		if(triada in frecuencias):
			last_position = frecuencias[triada][1][-1]
			frecuencias[triada][0] += 1
			frecuencias[triada][1].append(i)
			frecuencias[triada][2].append(i-last_position)
		else:
			frecuencias[triada] = [1,[i],[]]
	return frecuencias

archivo = open("HERALDOSNEGROS_pre.txt", 'r')
mensaje = archivo.read()

trigramas = kasiski(mensaje)

for x in trigramas:
	if(trigramas[x][0]>1):
		print(x,trigramas[x][2])