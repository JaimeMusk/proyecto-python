# importar #
import random
#saludo#
print('\t Welcome to the Coin Toss App.')
#inputs#
coin_toss_no = int(input('\tEnter ther number of times you want to flip the coin ? '))
toss_result = input('\tDo you want to see result of each toss ? (y/n) ').title()
#variables#
heads_count = 0
tails_count = 0

print('\n Flipping in colors!!')#estupideces mias#
#bucles#
for i in range(1,coin_toss_no+1):
    result = random.randint(0,1)
    if 'y' in toss_result:
        if result == 0 :
            print('\t Heads!')
        else:
            print('\t Tails!')    

    if result == 0:
        heads_count +=1
    elif result == 1:
        tails_count +=1

    if heads_count == tails_count:
        print(f'\tOh! At toss {i}, heads equals tails with {heads_count} each ')
#variable en porcentaje#
head_percent = round((heads_count/coin_toss_no) *100,2)
tail_percent = round((tails_count/coin_toss_no) *100,2)

print('\t Summary report')
print('\t Side \t\t Count \t\t Percentage ')
print(f'\t Head \t\t {heads_count} \t\t {head_percent}')
print(f'\t Tail \t\t {tails_count} \t\t {tail_percent}')