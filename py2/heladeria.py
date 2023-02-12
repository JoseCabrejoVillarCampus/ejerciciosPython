"""Escribe un programa que responda a un usuario que quiere comprar un helado en una conocida
marca de comida rápida cuanto le costará en función del topping que elija. El helado sin topping
cuesta 1.90€. El topping de oreo cuesta 1€. El topping de KitKat cuesta 1.50€. El topping de brownie
cuesta 0.75€. El topping de lacasitos cuesta 0.95€. En caso de no disponer del topping solicitado por
el usuario el programa escribirá por pantalla «no tenemos este topping, lo sentimos. » y a continuación
informar del precio del helado sin ningún topping."""

VALOR_BASE_HELADO = 1.9
opcionToping = input("Ingrese el topping: ").upper()

if (opcionToping == "OREO"):
    valorAgregado = 1
elif (opcionToping == "KITKAT"):
    valorAgregado = 1.5
elif (opcionToping == "BROWNIE"):
    valorAgregado = 0.75
elif (opcionToping == "LACASITOS"):
    valorAgregado = 0.95
else:
    valorAgregado = 0
    print("no tenemos este topping, lo sentimos.")

valorHelado = VALOR_BASE_HELADO + valorAgregado

print("El valor del helado es:", valorHelado,
      ", el topping seleccionado fue:", opcionToping)
