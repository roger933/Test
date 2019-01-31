def suma (num1,num2):

    resultado = num1+num2
    print ("El resultado es " ,resultado)

def resta (num1,num2):

    resultado = num1-num2
    print ("El resultado es " ,resultado)


print ("Calculadora")
print ("Elige una opcion: ")
print ("1. Sumar")
print ("2. Restar")
print ("3. Multiplicar")

opcion = input ("Seleccionar una opcion ")

if opcion == "1":
    num1 = int(input("Introduce el primer numero "))
    num2 = int(input("Introduce el segundo numero "))
    suma (num1,num2)
    
if opcion == "2":
    num1 = int(input("Introduce el primer numero "))
    num2 = int(input("Introduce el segundo numero "))
    resta (num1,num2)

if opcion == "3":
    num1 = int(input("Introduce el primer numero "))
    num2 = int(input("Introduce el segundo numero "))
    resultado = 0
 
for i in range(num1):
    resultado= resultado+num2  
 
print ("El resultado es " ,resultado)
    


    
    
