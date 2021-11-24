
  
#import#
import random
#saludo#
print('\tWelcome to Rock, Scissors, and papper app.')
#variables 1#
rounds = int(input('\t How many rounds would you like to play ? '))
moves = ['tijeras', 'piedra', 'papel']
#puntiacion#
user_score = 0 
AI_score = 0
#bucle#
for round in range(rounds):
    message = ""
    winner = ""

    print('\tRound \t\t player score \t\t AI score ')
    print(f'\t {round+1} \t\t {user_score} \t\t {AI_score}')

    AI_choice = random.choice(moves)
    user_choice = input('\t Enter your choice piedra, papel,  0 tijeras: ').lower().strip()
#movimiento de la IA#
    if user_choice in moves:
        print(f'\t AI_picked {AI_choice} and you picked {user_choice} ')
  #tijers3
        if AI_choice == 'tijeras' and user_choice == 'tijeras':
            message = "tijeras empata a  tijeras!"
            winner = "tie"
        elif AI_choice == 'tijeras' and user_choice == 'papel':
            message = "tijeras corta papel!"
            winner = "AI"
        elif AI_choice == 'tijeras' and user_choice == 'piedra':
            message = "piedra aplasta tijeras!"
            winner = "You WIN"
        
        #piedra#    
        elif AI_choice == 'piedra' and user_choice == 'piedra':
            message = "piedra choca piedra!"
            winner = "tie"
        elif AI_choice == 'piedra' and user_choice == 'tijeras':
            message = "piedra aplasta tijeras"
            winner= "AI"
        elif AI_choice == 'piedra' and user_choice == 'papel':
            message = "Papel enrolla la  piedra!"
            winner = "You WIN"
        #papel#    
        elif AI_choice == 'papel' and user_choice == 'papel':
            message = "papel empata papel!"
            winner = "tie"
        elif AI_choice == 'papel' and user_choice == 'tijeras':
            message = "tijeras corta papel "
            winner = "YOU WIN"
        elif AI_choice == 'papel' and user_choice == 'piedra':
            message = "papel enrolla piedra!"
            winner = "AI"
        else:
            print("Round not calculated")
            winner = "tie"                           
            message = "It's a tie how boring"

        print(f'\n\t {message} ')
        if winner == 'Player':
            print(f'\t Player wins the round {round+1}')
            user_score +=1
        elif winner == 'AI':
            print(f'\t AI wins the round {round+1}')
            AI_score +=1
        else:
            print('\t This round is a tie')
    else:
        print("That is not a valid game option!")
        print("IA gets the point!")
        AI_score += 1        

#resultadso#
print("\tFinal Game Results")
print(f"\tRounds Played: {rounds}")
print(f"\tPlayer Score: {user_score}")
print(f"\tAI Score: {AI_score}")
if user_score > AI_score:
    print("\tWinner: YOU WIN!!!")
elif AI_score > user_score:
    print("\tWinner: AI :-(")
else:
    print("\tThe game was a tie.")