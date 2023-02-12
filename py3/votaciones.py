# Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
# candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
# Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido 
# [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a 
# ninguno de los candidatos disponibles, indicar “Opción errónea”

print("opcion A ---> Partido Rojo")
print("opcion B ---> Partido verde")
print("opcion C ---> Partido Azul")
opcionVoto = input("Elija una de las opciones:\t").lower()

if(opcionVoto == "a"):
    print("Usted ha votado por el partido Rojo")
elif(opcionVoto == "b"):
    print("Usted ha votado por el partido Verde")
elif(opcionVoto == "c"):
    print("Usted ha votado por el partido Azul")
else:
    print("Opción errónea")

