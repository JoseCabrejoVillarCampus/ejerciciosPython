from os import system
system("cls")

listaNombreMedicamento = []
listaPrecioMedicamento = []



while True:
    print("------------ MENU -----------------")
    print('''    1 -> Agregar un medicamento
    2 -> Consultar precio de un medicamento
    3 -> Realizar una compra 
    4 -> Ver todos los medicamentos
    5 -> Salir ''')
    
    opcion = int(input("Ingrese la opcion a realizar: "))
    if(opcion==1):
        print("-------------- Agregar Medicamentos ----------------")
        bandera = True
        while bandera:
            nombreMedicamento = input("Ingrese el nombre del medicamento a almacenar: ")
            if(nombreMedicamento != "*"):
                precioMedicamento = int(input("Ingrese el precio del medicamento: "))
                listaNombreMedicamento.append(nombreMedicamento)
                listaPrecioMedicamento.append(precioMedicamento)
            else:
                bandera = False
        system("cls")
        
    elif(opcion==2):
        print("---------------- Consultar Precio ------------------")
        nombreMedicamento = input("Ingrese el nombre del medicamento a consultar: ")
        cantidadMedicamentos = len(listaNombreMedicamento)
        banderaNoExiste = True
        for x in range(cantidadMedicamentos):
            if(nombreMedicamento == listaNombreMedicamento[x]):
                print("El precio del medicamento",nombreMedicamento,"y su precio es:",listaPrecioMedicamento[x])
                banderaNoExiste = False
        if(banderaNoExiste):
            print("El medicamento",nombreMedicamento,"no existe")
        input("Presione cualquier tecla para continuar")
        system("cls")
        
    elif(opcion==3):
        print("---------------- Realizar Compra ------------------")
        totalCompra = 0
        while True:
            nombreMedicamento = input("Ingrese el nombre del medicamento a comprar: ")
            if(nombreMedicamento != "*"):
                cantidad = int(input("Ingrese la cantidad a comprar: "))               
                cantidadMedicamentos = len(listaNombreMedicamento)
                banderaNoExiste = True
                for x in range(cantidadMedicamentos):
                    if(nombreMedicamento == listaNombreMedicamento[x]):
                        precio = listaPrecioMedicamento[x]
                        totalCompra += precio*cantidad
                        banderaNoExiste = False
                if(banderaNoExiste):
                    print("El medicamento",nombreMedicamento,"no existe")     
            else:
                break
        print("El total a pagar es:",totalCompra)
        input("Presione cualquier tecla para continuar")  
        system("cls")
    elif(opcion==4):
        print("---------------- Ver Todos Medicamentos ------------------")
        print(listaNombreMedicamento)
        input("Presione cualquier tecla para continuar")
        system("cls") 
        
    elif(opcion==5):
        print("---------------------- Salir ----------------------")
        system("cls")
        break
    else:
        print("Error opcion no valida")
        system("cls")