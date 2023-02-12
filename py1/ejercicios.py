# Escribir una función  los elementos de una lista una cantidad n de veces. Por ejemplo, 
# replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

def replicar(lista,n):
    listaResultado = lista*n
    listaResultado.sort()
    print(listaResultado)
    
def replicarV2(lista,n):
    listaResultado = []
    for elementos in lista:
        for x in range(n):
            listaResultado.append(elementos)
    print(listaResultado)
        
    
# Crea una función que dados dos números mostrará todos los números que hay entre ellos.
def rango(inf,sup):
    for x in range(inf+1,sup):
        print(x)
        
# Crea una función que nos dibuje un cuadro en la pantalla con un ancho y alto dado
# ***********
# *         *
# *         *
# *         *
# *         *
# ***********

def cuadrado(ancho,alto):
    print("*"*ancho)
    for x in range(alto-2):
        print("*"+" " * (ancho-2) +"*")
    print("*"*ancho)
    
# Una compañía de helados ha creado un código para que se le introduzca el sabor del helado 
# automáticamente indique el precio:
# las opciones de helados son:
# 
# Sabor         Precio
# chocolate     5000
# fresa         3000
# mora          4000
# coco          3500


def precioHelado(sabor):
    if(sabor=="chocolate"):
        print(5000)
    elif(sabor=="fresa"):
        print(3000)
    elif(sabor=="mora"):
        print(4000)
    elif(sabor=="coco"):
        print(3500)
        
# Cree un algoritmo que nos permita saber cuantas veces se repite una palabra en una frase .

def tranformar(frase,caracter):
    print(frase.count(caracter))

# Cree un algoritmo que permita cambiar de cualquier cadena de texto que tenga el numero 2021 por 2022

def modificarFrase(frase,fraseOld,fraseNew):
    frase = frase.replace(fraseOld,fraseNew)
    print(frase)
    
# Cree un algoritmo que dada una cadena de texto la divida cuando se encuentre un (.)
frase = "dasdasd.asholadasd.asdasd"
frase = frase.split(".")
print(frase)

# Cree un algoritmo que le permita obtener el promedio de la siguiente lista [1,2,5,6,8,5,2,5,4,2,5,6,2,4,5,2,3,6,5,4,2,6,8,2,1,4,5,2,6,8,5,7,8,2,5,4]
lista = [1,2,5,6,8,5,2,5,4,2,5,6,2,4,5,2,3,6,5,4,2,6,8,2,1,4,5,2,6,8,5,7,8,2,5,4]
promedio = sum(lista)/len(lista)
print(promedio)

suma = 0
cantidad = 0
for numero in lista:
    suma += numero
    cantidad += 1
promedio = suma/cantidad
print(promedio)