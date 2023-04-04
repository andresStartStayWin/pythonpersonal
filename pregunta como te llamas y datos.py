print("Hola cómo te llamás?")
nombre = input()
print("Mucho gusto " + nombre)
print("El largo de tu nombre es:")
#print(len(nombre), " letras")

#contador de espacio en blanco
def espacios(nombre):
     
    contar = 0
     
    for i in nombre:
         
        if i == " ":
            contar += 1
         
    return contar
restar = espacios(nombre)
#ac  termina el contador de espacios

#al largo del nombre le resta los espacios
print(str(len(nombre) - int(restar)) + " letras")


print("Cuántos años tenés?")
edad = input()
print("Vas a tener " + str(int(edad) + 3) + " en 3 años")
print("Aceptás un desafío?")

desafio = input()
desafiosi = ["Si", "si", "s", "S", "yes", "Yes", "y", "Y"]
desafiono = ["No", "no", "n", "N"]

if desafio in desafiosi:
    print("Genial, que valiente!")
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
numrand2 = random.randint(0, 99)
print("La respuesta es ", numrand)

print("Está correcto?")
input()


print("Uh esperá!")
print("Me dí cuenta que tenía la calculadora en radianes!!!")


print("La suma TOTAL de ",num1, " + ", num2, " es " + str(int(num1) + int(num2)))

print(" ")
print("Ahora si? :D")
print("Bueno, eso es todo amigos, nos vemos en otra edición de NivelX con Bobby Goma!!")

#con este input te deja abierto el programa hasta apretar cualquier letra
input()
