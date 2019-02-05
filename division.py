def division (num1,num2):
    
    return num1 / num2
     
num1 = int(input("Introduzca el primer numero "))

num2 = int(input("Introduzca el segundo numero "))

try:
    resultado = division(num1,num2)

    print("El resultado es %d " % resultado)

except ZeroDivisionError:
        
    print("No se puede dividir entre 0")





