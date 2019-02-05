def division ():
    try:
        resultado = num1/num2

    except ZeroDivisionError:
        
        print("No se puede dividir entre 0")

    else:

        resultado=num1/num2

        return resultado

num1 = int(input("Introduzca el primer numero "))

num2 = int(input("Introduzca el segundo numero "))

resultado=division()

print("El resultado es " ,resultado)



