print("Hola cómo te llamás?")
nombre = input()
print("Mucho gusto " + nombre)
print("El largo de tu nombre es:")

#contador de espacio en blanco
def check_space(nombre):
     
    count = 0
     
    for i in nombre:
         
        if i == " ":
            count += 1
         
    return count
name = check_space(nombre)
#acá termina el contador de espacios

#al largo del nombre le resta los espacios
print(str(len(nombre) - int(name)) + " letras")


print("¿Cuántos años tenés?")
edad = input()
print("Vas a tener " + str(int(edad) + 3) + " en 3 años")
print("Aceptás un desafío?")


desafio = input()
desafiosi = ["Si", "si", "s", "S", "yes", "Yes", "y", "Y"]
desafiono = ["No", "no", "n", "N"]

if desafio in desafiosi:
    print("Genial, qué valiente!")
elif desafio in desafiono:
    print("Dijiste -No-, pero te lo digo igual :D")
else:
    print("Tenías que escribir si o no, pero igualmente te lo digo")
          
print("Escribí 2 números y te los sumo:")
print("Escribí el primero")
num1 = input()
print("Escribí el segundo")
num2 = input()

import random
numrand = random.randint(0, 99)
print("La respuesta es ", numrand)

print("Está correcto?")
input()

print("Era broma :D!")

print("La suma TOTAL es " + str(int(num1) + int(num2)))

#con éste input te deja abierto el programa
input()
