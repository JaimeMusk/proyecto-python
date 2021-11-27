# importamos random#
import random
#deinimos todas las funciones#
def dice_sides() ->int:
    sides = int(input('\t Enter the sides of the dice. : '))
    return sides

def dice_number() -> int:
    dice = int(input('\t How many dices would you like to roll : '))
    return dice

def roll_dice(dice_sides:int,dice_count:int) -> list:
    values = []
    print(f'\t Rolling {dice_count} dice with {dice_sides} sides each. ')
    for dice in range(dice_count):
        rolled_number = random.randint(1,dice_sides)
        values.append(rolled_number)
    return values    

def sum_dice(values:list) -> None:
    total = sum(values,0)
    print(f'\t Sum of all rolled dices {total}')

def roll_again() -> bool:
    response = input('\t Would you like to roll the dice again ? (y/n) ').title()
    if response.startswith('y'):
        return True
    else:
        return False

#programa #
if __name__ == "__main__":
    print('\t Welcome to the Dice Roll Game.')
    playing=True
    while playing:
       
        no_sides = dice_sides()
        no_dices = dice_number()

        rolled_values = roll_dice(no_sides,no_dices)
        sum_dice(rolled_values)
        playing = roll_again()
    print('\tSee you later<3!')  