#importar #
import random
#saludo#
print('\tWelcome to the guess number app.<3')
#variable3
name = input('\t Enter your name : ').title().strip()

print('\t I have choosen a number between 1 and 20. Can you guess the number ? ')
random_number = random.randint(1, 20)
#bucle y condicionales#
for i in range(1, 6):
    guessed_number = int(input('\t Guess a number between 1 and 20 : '))

    if guessed_number > 20:
        print('\t Choose a number between 1 and 20 : ')
    elif guessed_number < random_number:
        print(f'\t It is higher than {guessed_number} ')
    elif guessed_number > random_number:
        print(f'\t It is lower than {guessed_number}')
    else:
        break
if guessed_number == random_number:
    print(f'\t Yeah!{name}, You guessed it correct in {i}º time.Congrats ')
else:
    print(f'\t Game over! The correct number was {random_number}, nice try')   