i = 0
while i < 10:
    i = i + 1
    print(i)

def fun(var):
    contador = 0
    for i in var:
        if i == " ":
            contador += 1
    return contador
var = input()
print(fun(var))
