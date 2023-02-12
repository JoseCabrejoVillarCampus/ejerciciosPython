from os import system

dbColegio = [{"usuario":"admin","nombre":"daniela","apellido":"ortiz","rol":"administrador","estado":True}]

dbNotas = []

def AgregarUsuario(rol):
    cantidadUsuarios = int(input("Cuantos "+rol+" desea agregar: "))
    for x in range(cantidadUsuarios):
        nombre = input("Ingrese el nombre del "+rol+": ")
        apellido = input("Ingrese el apellido del "+rol+": ")
        nombreUsuario = input("Ingrese el nombre de usuario del "+rol+": ")
        contraseña = input("Ingrese la contraseña del "+rol+": ")
        estado = input("Ingrese el estado del "+rol+" (activo o inactivo): ").lower()
        if(estado == "activo"): 
            usuarioDic = {"usuario":nombreUsuario,"contraseña":contraseña,"nombre":nombre,"apellido":apellido,"rol":rol,"estado":True}
        else:
            usuarioDic = {"usuario":nombreUsuario,"contraseña":contraseña,"nombre":nombre,"apellido":apellido,"rol":rol,"estado":False}
        dbColegio.append(usuarioDic)
    
def EliminarUsuario(rol):
    nombreUsuario = input("Ingrese el nombre de usuario del "+rol+" a eliminar: ")
    for usuario in dbColegio:
        if(usuario["rol"] == rol and usuario["usuario"] == nombreUsuario):
            dbColegio.remove(usuario)
            
def ModificarUsuario(rol):
    nombreUsuario = input("Ingrese el nombre de usuario del "+rol+" a eliminar: ")
    for usuario in dbColegio:
        if(usuario["rol"] == rol and usuario["usuario"] == nombreUsuario):
            nombre = input("Ingrese el nombre del "+rol+": ")
            apellido = input("Ingrese el apellido "+rol+": ")
            estado = input("Ingrese el estado (activo o inactivo) del "+rol+": ")
            contraseña = input("Ingrese la contraseña del "+rol+": ")
            usuario["nombre"] = nombre
            usuario["apellido"] = apellido
            usuario["contraseña"] = contraseña
            if(estado == "activo"): 
                usuario["estado"] = True
        else:
            usuario["estado"] = False

def ObtenerUsuario(rol):
    for usuario in dbColegio:
        if(usuario["rol"] == rol):
            print(usuario)
            
while True:
    system("cls")
    print(''' 
          1. Menu Administrador
          2. Menu Rector
          3. Menu Docente
          4. Menu Estudiante
          5. Salir''')
    try:
        opcion = int(input("Seleccione una opcion: "))
        
        if(opcion == 1):
            print("Menu de administrador")
            while True:
                system("cls")
                print(''' 
                1. Agregar 
                2. Modificar
                3. Eliminar
                4. Listar
                5. Regresar a Menu principal
                ''')
                try:
                    opcion = int(input("Seleccione una opcion: "))
                    if(opcion == 1):
                        print("Agregar")
                        while True:
                            system("cls")
                            print(''' 
                                1. Rector 
                                2. Docente
                                3. Estudiante
                                4.  Regresar a menu administrador
                                ''')
                            try:
                                opcion = int(input("Seleccione una opcion: "))
                                if(opcion == 1):
                                    AgregarUsuario("rector")
                                elif(opcion == 2):
                                    AgregarUsuario("docente")
                                elif(opcion == 3):
                                    AgregarUsuario("estudiante")
                                elif(opcion == 4):
                                    print("Regresar a menu administrador")
                                    break
                                else:
                                    print("opcion no valida")
                            except:
                                print("Error, tipo de opcion no valido")    
                    elif(opcion == 2):
                        print("Modificar")
                        while True:
                            system("cls")
                            print(''' 
                                1. Rector 
                                2. Docente
                                3. Estudiante
                                4.  Regresar a menu administrador
                                ''')
                            try:
                                opcion = int(input("Seleccione una opcion: "))
                                if(opcion == 1):
                                    ModificarUsuario("rector")
                                elif(opcion == 2):
                                    ModificarUsuario("docente")
                                elif(opcion == 3):
                                    ModificarUsuario("estudiante")
                                elif(opcion == 4):
                                    print("Regresar a menu administrador")
                                    break
                                else:
                                    print("opcion no valida")
                            except:
                                print("Error, tipo de opcion no valido")
                    elif(opcion == 3):
                        print("Eliminar")
                        while True:
                            system("cls")
                            print(''' 
                                1. Rector 
                                2. Docente
                                3. Estudiante
                                4.  Regresar a menu administrador
                                ''')
                            try:
                                opcion = int(input("Seleccione una opcion: "))
                                if(opcion == 1):
                                    EliminarUsuario("rector")
                                elif(opcion == 2):
                                    EliminarUsuario("docente")
                                elif(opcion == 3):
                                    EliminarUsuario("estudiante")
                                elif(opcion == 4):
                                    print("Regresar a menu administrador")
                                    break
                                else:
                                    print("opcion no valida")
                            except:
                                print("Error, tipo de opcion no valido")
                    elif(opcion == 4):
                        print("Listar")
                        print("Agregar")
                        while True:
                            system("cls")
                            print(''' 
                                1. Rector 
                                2. Docente
                                3. Estudiante
                                4.  Regresar a menu administrador
                                ''')
                            try:
                                opcion = int(input("Seleccione una opcion: "))
                                if(opcion == 1):
                                    ObtenerUsuario("rector")
                                elif(opcion == 2):
                                    ObtenerUsuario("docente")
                                elif(opcion == 3):
                                    ObtenerUsuario("estudiante")
                                elif(opcion == 4):
                                    print("Regresar a menu administrador")
                                    break
                                else:
                                    print("opcion no valida")
                            except:
                                print("Error, tipo de opcion no valido")    
                            input()
                    elif(opcion == 5):
                        print("Regresar a Menu principal")
                        break
                    else:
                        print("opcion no valida")   
                except:
                    print("Error, tipo de opcion no valido")
                input()
                    
        elif(opcion == 2):
            print("Menu de rector")
            
        elif(opcion == 3):
            print("Menu de docente")
            # {"usuario": "camila15" , "notas":[5,4,2,3]}
            while True:
                print(''' 
                    1. Asignar Notas
                    2. Regresar
                    ''')
                try:
                    opcion = int(input("Seleccione una opcion: "))  
                    if(opcion == 1):
                        notas = []
                        print("Asignar notas")
                        nombreUsuario = input("Ingrese el nombre del estudiante a asignar notas: ")
                        for usuario in dbColegio:
                            if(usuario["usuario"] == nombreUsuario and usuario["rol"] == "estudiante"):
                                for x in range(4):
                                    nota = float(input("Ingrese la nota: "))
                                    notas.append(nota)
                                notasDic = {"usuario":usuario["usuario"],"notas":notas}
                                dbNotas.append(notasDic)  
                                    
                    elif(opcion == 2):
                        print("Regresar a Menu principal")
                        break
                    else:
                        print("opcion no valida")   
                except:
                    print("Error, tipo de opcion no valido")
            
        elif(opcion == 4):
            print("Menu de estudiante")
            nombreUsuario = input("ingrese el nombre para ver las notas: ")
            for estudianteNotas in dbNotas:
                if(estudianteNotas["usuario"] == nombreUsuario):
                    print(estudianteNotas)
            input()
            
        elif(opcion == 5):
            print("Salir")
            break
        else:
            print("opcion no valida")
    except:
        print("Error, tipo de opcion no valido")
    
    input()