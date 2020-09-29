import operator

archivo = open("HERALDOSNEGROS_pre.txt", 'r')

def frecuencias(archivo):
	mensaje = archivo.read()

	diccionario = {}

	tamaño = len(mensaje)

	for i in range(tamaño):
		try:
			diccionario[mensaje[i]] += 1
		except:
			diccionario[mensaje[i]] = 1

	return diccionario

diccionario = frecuencias(archivo)

print("Diccionario: ")
print(diccionario)

sort_diccionario = sorted(diccionario.items(), 
	key=operator.itemgetter(1), reverse=True)

print("\nLas 5 letras que mas se repiten son")
for i in range(5):
	print(sort_diccionario[i])
