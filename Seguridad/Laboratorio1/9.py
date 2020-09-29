archivo = open("HERALDOSNEGROS_pre.txt", 'r')
mensaje = archivo.read()
correccion = ""

for i in range(0,len(mensaje),20):
	sub_msg = mensaje[i:i+20]
	if(len(sub_msg)<20):
		break
	correccion += sub_msg + "AQUÍ"

if(len(correccion)%4!=0):
	correccion += "X"*len(correccion)%4

f=open("HERALDOSNEGROS_pre.txt","w")
f.write(correccion)
f.close()
