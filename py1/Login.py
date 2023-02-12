# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es
# “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer 
# login incremente este valor.

# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres 
# oportunidades para intentarlo.

def Login(usuarioDB,contrasenaDB,intentos):
    for x in range(1,intentos+1):
        nombre = input("Ingrese el nombre del usuario: ")
        contrasena = input("Ingrese la contraseña del usuario: ")
        if(contrasena==contrasenaDB and nombre==usuarioDB):
            return True,"Credenciales correctas",nombre
            
        else:
            print("Le quedan:",(intentos-x))
        
    return False,"Credenciales incorrectas",None   
    



    
    
