#cargamos la funcion
def funcion(variable):

    #cargamos el contador
    contador = 0

    #cargamos el pedido
    for x in variable:

        #definimos la condicion
        if x == "h":

            #si encuentra h, suma 1
            contador += 1

    #y devuelve el nuevo estado del contador
    return contador

#la variable puede ser ya dada, o crearla con input()

##opciones
##print("Escribí la cantidad de h que quieras") 
##variable = input()
variable = "hola hola hola hhh"

#para mostrar el resultado, imprimimos la función
print(funcion(variable))
