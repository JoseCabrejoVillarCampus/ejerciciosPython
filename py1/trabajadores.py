# Crea un algoritmo que solicite el nombre, salario y cedula de distintos empleados hasta que el usuario lo desee, si el empleado
# gana por encima de 1 millón se le descuenta el 1.5% de su salario, si su cedula termina en un numero par se le sumara un 3% al 
# salario. Imprima para cada empleado su nuevo salario y el total a pagar por todos los trabajadores.
terminar = "no"
SALARIO_DESCUENTO = 1000000
totalNomina = 0
while True:
    if(terminar == "si"):
        break
    elif(terminar == "no"):
        nombreEmpleado = input("Ingrese el nombre del empleado: ")
        cedulaEmpleado = int(input("Ingrese la cedula del empleado: "))
        salarioEmpleado = float(input("Ingrese el salario del empleado: "))
        if(salarioEmpleado > SALARIO_DESCUENTO):
            salarioEmpleado = salarioEmpleado - salarioEmpleado*0.015
        if((cedulaEmpleado % 2) == 0):
            salarioEmpleado = salarioEmpleado + salarioEmpleado*0.03
        print("El emplado",nombreEmpleado,"con cedula",cedulaEmpleado,"gana",salarioEmpleado)
        totalNomina += salarioEmpleado
    else:
        print("Debe ser si o no")
    terminar = input("¿Quiere terminar (si): ").lower()
print("El total a pagar en nomina es:",totalNomina)