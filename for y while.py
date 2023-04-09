i = 0
while i < 10:
    i = i + 1
    print(i)

def funcion(variable):
    cont = 0
    for i in variable:
        if i == " ":
            cont += 1
    return cont
variable = input()
print(funcion(variable))
