class Cifrado_Examen(object):

    def __init__(self, key = 0):
        self.__key = key

    def encriptar(self,content):

        key = self.__key

        while (key > 255):
            key -= 255

        msg_encryp = ""

        for ch in content:
            msg_encryp += chr(ord(ch) ^ key)

        ans = ""
        for i in range(key % len(msg_encryp), len(msg_encryp)):
            ans += msg_encryp[i]

        for i in range(key % len(msg_encryp)):
            ans += msg_encryp[i]

        return ans

    def desencriptar(self,content,key = 0):

        key = self.__key

        while (key > 255):
            key -= 255

        msg_transpuesto = ""

        for i in range(len(content) - (key % len(content)), len(content)):
            msg_transpuesto += content[i]

        for i in range(len(content) - (key % len(content))):
            msg_transpuesto += content[i]

        ans = ""

        for ch in msg_transpuesto:
            ans += chr(ord(ch) ^ key)

        return ans

crypt = Cifrado_Examen(key=45678)

msg_claro = "Este es un texto largo, para probar como funciona el algoritmo con una llave de 45678"
msg_crypt = crypt.encriptar(msg_claro)
msg_decrypt = crypt.desencriptar(msg_crypt)

print("Msg Claro: ", end="")
print(msg_claro)
print("Msg Cifrado: ", end="")
print(msg_crypt)
print(f"Msg Descifrado: {msg_decrypt}")