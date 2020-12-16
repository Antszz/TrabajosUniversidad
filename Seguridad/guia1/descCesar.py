import unidecode

archivo = open("textoLabRes.txt", 'r')
mensaje = archivo.read()
archivo.close()

archivo = open("refer.txt", 'r')
mensaje2 = archivo.read()
mensaje2 = mensaje2.strip()
mensaje2 = mensaje2.replace(" ","")
mensaje2 = unidecode.unidecode(mensaje2)
mensaje2 = mensaje2.upper()
diccMensaje = mensaje2.split("\n")
archivo.close()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):

    translated = ''

    for symbol in mensaje:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = (num - key) % 26

            translated = translated + LETTERS[num]

        else:
            translated = translated + symbol

    countDicc = len(diccMensaje)
    for msg in diccMensaje:
        if msg in translated:
            countDicc -= 1
    if not countDicc:
        print('Key = %s: %s' % (key, translated))