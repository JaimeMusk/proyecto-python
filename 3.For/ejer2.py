#Saludo#
print('\n Welcome to Quadratic Equation Solver. ')
import cmath


#Funcion/operacion#
def quadratic_equation(a:float,b:float,c:float):
    x1 = (-b + cmath.sqrt( b**2 - 4*a*c))/(2*a)
    x2 = (-b + cmath.sqrt( b**2 - 4*a*c))/(2*a)
    return x1,x2
variables = int(input('''\n How many quadratic equations would you like to solve, 
print ask for the coefficients of the equation in the standard form of ax 2 + b x + c = 0 , : '''))

#variables#
for i in range(variables):
    print(f'Solving Equation #{i+1}')
    
    a = float(input('\tEnter the value of a (coefficient of X^2) :  '))
    b = float(input('\tEnter the value of b (coefficient of X) :  '))
    c = float(input('\tEnter the value of c (coefficient) : '))
    #operacion#
    x1, x2 = quadratic_equation(a,b,c)
    print(f"\nThe solutions to {a}x^2+{b}x+{c} = 0 are: ")
    print("\n\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))




