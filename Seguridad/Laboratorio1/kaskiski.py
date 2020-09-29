def buscar(palabra, distancia, texto, longitud_palabra):
    dic = {'palabra': palabra, 'repeticion': 0, 'distancias': []}
    for i in range(len(texto)):
        #if palabra == texto[i:i+longitud_palabra] and not i - distancia == 0 and i > distancia:
        if palabra == texto[i:i+longitud_palabra] and not i - distancia == 0:
            dic['repeticion'] += 1
            dic['distancias'].append(i - distancia)
            distancia = i
    return dic

def frecuencia(texto, long_palabra):
    lista_palabras = []

    for i in range(len(texto)):
        if len(texto[i:i+long_palabra]) == long_palabra:
            palabra = texto[i:i+long_palabra]
            dic = buscar(palabra, i, texto, long_palabra)
            if not dic.get('repeticion') == 0:
                if len(lista_palabras) == 0:
                    lista_palabras.append(dic)
                else:
                    dic_repetido = 0
                    for dic_temp in lista_palabras:
                        if dic_temp.get('palabra') == palabra:
                            dic_repetido += 1
                    if dic_repetido == 0:
                        lista_palabras.append(dic)

    return lista_palabras

xD = (3,[1,2,3],[1,1])
xD[0] = 4
print(xD[0])