archivo_texto=open("adventofcode1.txt", "r")

suma=0

for line in archivo_texto.readlines():

    suma = suma + int(line)

print (suma)
    



