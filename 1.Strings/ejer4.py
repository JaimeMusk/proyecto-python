print('Welcome to the right Triangle  Solver App')#Saludamos al usuario#


from math import sqrt #importamos el sqrt#
print("what is the lengths of shorter triangle sides:")#preguntas#
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )