"""Hacer un programa en python para una tienda de zapatos que tiene una promoción de descuento para 
vender al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les 
dará un 10% de descuento sobre el total de la compra; si el número de zapatos es mayor de veinte 
pero menor de treinta, se le otorga un 20% de descuento; y si son treinta o mas zapatos se otorgará un 40% 
de descuento. El precio de cada par de zapato es de $120.000."""

VALOR_ZAPATO = 120000
cantidadZapatos = 52
totalFactura = VALOR_ZAPATO*cantidadZapatos
descuento = 0
if (cantidadZapatos > 10):
    if (cantidadZapatos >= 20):
        if (cantidadZapatos >= 30):  # rango >= 30
            descuento = totalFactura*0.4
        else:  # rango [20 - 30)
            descuento = totalFactura*0.2
    else:  # rango (10-20]
        descuento = totalFactura*0.1
totalFactura -= descuento
print("El total a pagar es: ", totalFactura, "con un descuento de:", descuento)
