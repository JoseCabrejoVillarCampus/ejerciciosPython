# Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. 
# Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir 
# entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo 
# (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

print("opcion T ---> Triangulo")
print("opcion C ---> Circulo")
figura = input("Ingrese la opcion:\t").upper()

if(figura == "T"):
    base = float(input("Ingrese la base del triangulo"))
    altura = float(input("Ingrese la altura del triangulo"))
    area = base*altura/2
    print("El area del triangulo es",area)
elif(figura == "C"):
    radio = float(input("Ingrese el radio del circulo"))
    area = 3.141592*radio**2
    print("El area del circulo es",area)
else:
    print("No tenemos esa figura")