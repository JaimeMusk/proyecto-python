#saludo al ususario#
import math

print('\nWelcome to Factorial App <3')
#variable#
number = int(input('\tEnter ther number you want factorial for :  '))
#operacion1#
print(f'{number}! = ',end="")
for i in range(1, number):
    print(f'{i}', end="*")
print(f'{number}')    

print(f'\n Factorial using library : {math.factorial(number)}')
#factorial#
def factorial(number : int):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact
#Resultado#
result = factorial(number)
print(f'\n Factorial using own method : {result}')

print("\nIts shown twice that " + str(number) + "! = " + str(result) + " (with excitement!)")