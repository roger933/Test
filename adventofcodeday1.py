with open("adventofcode1.txt", "r") as archivo_texto:

    suma=0

    for line in archivo_texto.readlines():

        suma=suma+int(line)

print(suma)
    



