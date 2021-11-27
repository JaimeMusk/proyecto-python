#Funciones#

def get_info():
   #Saludo#
    print('\t Welcome to the Fake Bank. ')
    name = input('\t Please enter your name. ')
    savings_account_bal = float(input(f'\t hi {name}, enter your initial deposit with savings account '))
    checking_account_bal = float(input(f'\t hi {name} enter your initial deposit with checking account '))
#info#
    user_info = {
        "user_name": name,
        "savings" : savings_account_bal,
        "checking" : checking_account_bal
    }
    return user_info

def make_deposit(bank_details : dict, acc_type: str, amount : float ):
    bank_details[acc_type] += amount
    print(f'\t {amount} added to your {acc_type} account. Total amount {bank_details[acc_type]}.')

def make_withdrawl(bank_details : dict, acc_type: str, amount:float):
    current_bal = bank_details[acc_type]
    current_bal -= amount

    if(current_bal > 0) :
        print(f'\t Transaction was successful')
        bank_details[acc_type] -= amount
        print(f'\t Updated balance in {acc_type} is {bank_details[acc_type]}')
    else :
        print(f'Insufficient balance to make this transaction.')        

def display_info(bank_details: dict):
    print('\t -------------- Account Summary -------------------')
    print(f'\t Name : {bank_details["user_name"]}')
    print(f'\t Savings : {bank_details["savings"]}')
    print(f'\t Checking : {bank_details["checking"]}')
#programa#
if __name__ == "__main__":
  details = get_info()
  running= True 
  while running:
     acc_type : str= ""
     trans_type : str = ""
     amount : float= 0.0
     
     display_info(details)

     acc_type = input('\t Choose tha account type (checking/savings) ').lower()
     trans_type = input('\t Choose the type of transactions (withdrwal/deposit) ').lower() 
     amount = float(input('\t Enter the ammount'))

     if acc_type.startswith('c') :
         if trans_type.startswith('w'):
             make_withdrawl(details,'checking', amount)
         elif trans_type.startswith('d'):
             make_deposit(details, 'checking', amount)
         else:
             print('Invalid selection!')        
     elif acc_type.startswith('s'):
         if trans_type.startswith('w'):
             make_withdrawl(details,'savings', amount)
         elif trans_type.startswith('d'):
             make_deposit(details, 'savings', amount)
         else:
             print('Invalid selection!')
     else :
         print('Invalid Selection')    

     continue_app = input('\t Would you like to make another transaction ? (Y/N). ').lower()
     if continue_app.startswith('n'):
         display_info(details)
         print('\t Thank you ,see you later.')
         running =False  