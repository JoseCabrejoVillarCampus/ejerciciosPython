"""Hacer un programa en python para una tienda de zapatos que tiene una promoción de descuento para 
vender al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les 
dará un 10% de descuento sobre el total de la compra; si el número de zapatos es mayor de veinte 
pero menor de treinta, se le otorga un 20% de descuento; y si son treinta o mas zapatos se otorgará un 40% 
de descuento. El precio de cada par de zapato es de $120.000."""

VALOR_ZAPATO = 120000 # Constante con el precio del zapato
cantidadZapatos = int(input("Ingrese la cantidad de zapatos: ")) # input permite ingresar datos 
totalFactura = VALOR_ZAPATO*cantidadZapatos # realizamos la operacion matematica
descuento = 0   # variable para almacenar el descuento aplicado
if (cantidadZapatos >= 30):  # rango >= 30
    descuento = totalFactura*0.4 # descuento de 40% para 30 o mas zapatos 
elif (cantidadZapatos >= 20):  # rango [20-30)
    descuento = totalFactura*0.2 # descuento de 20% para 20 a 29 zapatos 
elif (cantidadZapatos >= 10):  # rango [10-20)
    descuento = totalFactura*0.1 # descuento de 10% para 10 a 19 zapatos 
totalFactura -= descuento # aplicamos el descuento al total de la factura
print("El total a pagar es: ", totalFactura, "con un descuento de:", descuento) # mostramos en pantalla el resultado

#Nota1: totalFactura -= descuento    es lo mismo que     totalFactura = totalFactura - descuento
#Nota2: input siempre retorna el valor ingresado por el usuario en un tipo de dato String o cadena de texto
#Nota3: elif permite realizar mas preguntas y se debe cumplir siempre con el orden if - elif - else
#Nota4: puede agregar la cantidad de elif que sean necesarios
#Nota5: en la linea 8 la funcion int() permite convertir un string a un int a eso se le conoce como casting
 