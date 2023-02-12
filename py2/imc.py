"""
Calcule el valor de IMC e imprima la clasificación
IMC = peso (kg) / altura 2 (m2)

 [0 - 18.5) -----> Delgado
 [18.5 - 25) -----> Normal
 [25 - 30) ------> Exceso de peso
 [30 - inf] -----> Obesidad

 Salida: El valor del IMC es: 15BMI, nuestra clasificacion es Delgado
    1, input    2. casting    3. and or not   4. try except

"""
try:
    print("Solo se permite numeros")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en m: "))
    imc = peso/altura**2
    if (imc >= 0):
        if (imc >= 0 and imc < 18.5):
            categoria = "Delgado"
        elif (imc >= 18.5 and imc < 25):
            categoria = "Normal"
        elif (imc >= 25 and imc < 30):
            categoria = "Exceso de peso"
        else:
            categoria = "Obesidad"

        print("El valor del IMC es:", round(imc, 3), "BMI",
              "nuestra clasificacion es:", categoria)

    else:
        print("IMC negativo")
except:
    print("El tipo de dato no es valido")

print("gracias", "Adios")
