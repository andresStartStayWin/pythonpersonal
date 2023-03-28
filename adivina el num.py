# This is a guess the number game
import msvcrt
import random


print('Hola, cuál es tu nombre?')
name = input()

print('Bueno, ' + name + ', estoy pensando en un número entre 1 y 20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Adiviná')
    guess = int(input())

    if guess < secretNumber:
        print('Muy bajo')
    elif guess > secretNumber:
        print('Eee, muy alto')
    else:
        break #esta condicion es para cuando acertás

if guess == secretNumber:
    print('Bien! ' + name + ', adivinaste el número en ' + str(guessesTaken) + ' veces')
else:
    print('No, el número era ' + str(secretNumber))

msvcrt.getch()
