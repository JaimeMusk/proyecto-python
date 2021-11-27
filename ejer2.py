#Definimos las Funciones#

def add(a:float, b:float) -> float:
    print('\t performing addition operation ')
    return f'{a}+{b} = {round(a+b,4)}'
def subtract(a:float, b:float) -> float:
    print('\t performing subtraction operation ')
    return f'{a}-{b} = {round(a-b,4)}'
def multiply(a:float, b:float) -> float:
    print('\t performing multiplication operation ')
    return f'{a}*{b} = {round(a*b,4)}'
def division(a:float, b:float) -> float:            
    print('\t performing division operation ')
    if b == 0:
        print('\t You cannot divide by zero.')
        raise Exception('Error: DIV ERROR')
    else:
        return f'{a}/{b} = {round(a/b,4)}'
def exponent(a:float, b:float) -> float:
    print('\t Performing exponential operation')
    return f'{a} ** {b} = {round(a**b,)}'

def continue_app() ->bool:
    response = input('\n Do you want to continue ? (y/n):').title()
    if response.startswith('y'):
        return True
    else:
        return False    
#programa#
if __name__ == "__main__":
    print('\t Welcome to the basic calculator app. ')
    active=True
    history = []
    while active:
        inputs = input('\t Enter the numbers comma separated : ').split(',')
        operation = input('\t Enter the type of operation you want to perform :').title()
        arg_one = float(inputs[0])
        arg_two = float(inputs[1])
        if operation.startswith('a'):
            result = add(arg_one,arg_two)
            print(f'\t {result}')
        elif operation.startswith('s'):
            result = subtract(arg_one,arg_two)
            print(f'\t {result}')
        elif operation.startswith('m'):
            result = multiply(arg_one,arg_two)
            print(f'\t {result}')        
        elif operation.startswith('d'):
            try:
                result = division(arg_one,arg_two)
                print(f'\t {result}')
            except Exception as e :
                result = f'\t {e}'

        elif operation.startswith('e'):
            result = exponent(arg_one,arg_two)
            print(f'\t {result}')
        else:
            result = 'Invalid Operations. Operation not supported.'
            print(f'\t {result}') 
        history.append(result)
        active=continue_app()
    print('Summary of your operations :')
    for operation in  history:
        print(f'\t {operation}')        
    print('\t Thank you ,see you later.')