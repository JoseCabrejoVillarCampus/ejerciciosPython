# Escribir un programa que almacene la cadena de caracteres relacionada a una contraseña 
# en una constante, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable sin tener 
# en cuenta mayúsculas y minúsculas

CONTRASENA = "MisionTic2022+*".lower()
contrasenaUsuairo = input("Ingrese su contraseña:\t").lower()

if (CONTRASENA == contrasenaUsuairo):
    print("Contraseña correcta")
else: 
    print("Contraseña incorrecta")



