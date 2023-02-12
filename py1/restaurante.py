
from os import system

system("cls") #clear mac o linux

listaHamburguesas = [["Hamburguesa","Mexicana",20000],["Hamburguesa","Hawaiana",18000],["Hamburguesa","Doble carne",23000],["Hamburguesa","Argentina",16000],["Hamburguesa","Junior",10000]]
listaPizza = [["Pizza","Mexicana",13000],["Pizza","Hawaiana",10000],["Pizza","Carnes",12000],["Pizza","Pollo",12000]]
listaBurritos = [["Burrito","Carne al pastor",13000],["Burrito","Pollo carne",10000],["Burrito","Frijol refrito",12000]]

listaCompras = []


while True:
    print("""----------- Menu principal -----------------
    1 -> Hamburguesas
    2 -> Pizzas
    3 -> Burritos
    4 -> Calcular compra
    5 -> Salir"""
    )
    
    opcion = int(input("Seleccione una opcion: "))

    if(opcion == 1):
        print("Menu Hamburguesas")
        print('''    1 -> Mexicana -------------- 20000
    2 -> Hawaiana -------------- 18000
    3 -> Doble carne ----------- 23000
    4 -> Argentina ------------- 16000
    5 -> Junior ---------------- 10000
    6 -> Regresar ''')
        while True:
            try:
                opcionCompra = int(input("Seleccione la opcion de hamburguesa: "))
                if(opcionCompra == 6):
                    break
                elif(opcionCompra > 6 or opcionCompra <= 0):
                    print("opcion no valida")
                else:
                    listaCompras.append(listaHamburguesas[opcionCompra-1])
            except:
                print("Error opcion no valido") 
    elif(opcion == 2):
        print("Menu Pizzas")
        print('''    1 -> Mexicana -------------- 13000
    2 -> Hawaiana  ------------- 10000
    3 -> Carnes------- --------- 12000
    4 -> Pollo ----------------- 12000
    5 -> Regresar
    ''')
        while True:
            try:
                opcionCompra = int(input("Seleccione la opcion de pizza: "))
                if(opcionCompra == 5):
                    break
                elif(opcionCompra > 5 or opcionCompra <= 0):
                    print("opcion no valida")
                else:
                    listaCompras.append(listaPizza[opcionCompra-1])
            except:
                print("Error opcion no valido")    
    elif(opcion == 3):
        print("Menu Burritos")
        print('''    1 -> Carne al pastor -------------- 13000
    2 -> Pollo carne ----------------- 10000
    3 -> Frijol refrito -------------- 12000
    4 -> Regresar
    ''')
        while True:
            try:
                opcionCompra = int(input("Seleccione la opcion de burritos: "))
                if(opcionCompra == 4):
                    break
                elif(opcionCompra > 4 or opcionCompra <= 0):
                    print("opcion no valida")
                else:
                    listaCompras.append(listaBurritos[opcionCompra-1])
            except:
                print("Error opcion no valido")
        
    elif(opcion == 4):
        print("Calcular compra")
        totalCompra = 0
        for productos in listaCompras:
            print(productos[0],"---",productos[1],"-------",productos[2])
            totalCompra += productos[2]
        
        print("El total a pagar es:",totalCompra)        
        
        
    elif(opcion == 5):
        print("Salir")
        break
    else:
        print("Opcion no valida")
    