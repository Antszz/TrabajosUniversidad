b=-1
for i in range(27):
	a = (5*i)%27
	if(a==1):
		b=i
	print(f"{i} = {a}")

print(f"El inverso multiplicativo de 5 es {b}")