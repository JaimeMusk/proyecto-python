<<<<<<< HEAD
print('Welcome to the Letter Counter App')
name = input('What is your name?: ')
print('Hellow {name}!\nI will  count the number of times thaht specific letter  occurs  in a message.')
message = input('Please enter a message')
count = input('Wich letter would you like  to count the ocurrences of: ')
=======
print("welcome to the Grade Sorter App!")#saludo3
print("introduce 4 notas (0-100)")
#variables#
n1 = input("nota1 :")
n2 = input("nota2 :")
n3 = input("nota3 :")
n4 = input("nota4 :")
#Append#
notas = []
notas.append(n1)
notas.append(n2)

notas.append(n3)
notas.append(n4)
#Ordenar y eliminar notas de mayor a menor#
notas_p = sorted(notas,reverse = True)
print("tus notas de mayor a menor son :", notas_p)


print("hemos eliminado la nota :", notas_p.pop(3))
print("y :", notas_p.pop(2))

print("las dos notas mayores son :", notas_p)
print("la mejor nota es :", notas_p[0])
>>>>>>> 7da2e9f4f966b18fe1a907fb54b2fecb4d6b09ad
