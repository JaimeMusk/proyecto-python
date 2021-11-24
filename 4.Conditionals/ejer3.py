#saludo#

print('\t Welcome to voter registration app!')
name = input('\t Enter your name please : ')
age = int(input('\t What is your age ? '))
#partidos para nada corruptos#
parties = ['democratas, republicanos', 'independentistas', 'Green']
#Condicional#
if age > 17:
    print(f'\t Congratulations! {name} You are old enough to vote.')
#bucle + candicional#
    print('\t Available parties :')
    for i in parties:
         print(f'\t {i}')
#condicional del partido del usuario#
    user_choice = input('\t Pick a party (corrupt )to join : ').title()
    if user_choice == 'democratas':    
        print(f'\ttCongratulations you have joined {user_choice}, which is a major party of America., except party of Trump, Because is God')
    elif user_choice == 'republicanos':    
        print(f'\t Congratulations you have joined {user_choice}, which is a major party of America.except party of Trump, Because is God')    
    elif user_choice == 'independents':    
        print(f'\t Congratulations you have joined {user_choice}, which is a individual party of America.except party of Trump, Because is God')
    elif user_choice == 'green':    
        print(f'\t Congratulations you have joined {user_choice}, which is a minor party of America.except party of Trump, Because is God')    
    else:
        print(f'\t This corrupt  party doesnt exists!<3')    
else:
    print(f'\t Sorry! {name}, you are not old enough to vote, try other year <3')    