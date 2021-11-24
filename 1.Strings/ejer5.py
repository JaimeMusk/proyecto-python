<<<<<<< HEAD
print('Welcome to the Multiplication/Exponent Table App')##saludamos al usuario##
name = input('\nWhat is your name: ').title()#pregunto nombre#
num = float(input('What namber want you like to work with: '))#pregunta numero para trabajar#
msg = name + ',Math is cool'#agradecimiento#

print(f'\nMultiplication Table For {num}')#tabla de multiplicar y operaciones+ #
print(f'\n\t1.0*{num}={round(1*num,4)}\n\t2.0*{num}={round(2*num,4)}\n\t3.0*{num}={round(3*num,4)}\n\t4.0*{num}={round(4*num,4)}\n\t5.0*{num}={round(5*num,4)}\n\t6.0*{num}={round(6*num,4)}\n\t7.0*{num}={round(7*num,4)}\n\t8.0*{num}={round(8*num,4)}\n\t9.0*{num}={round(9*num,4)}')
print(f'\nExponent Table For {num}')
print(f'\n\t{num}**1={round(num**1,4)}\n\t{num}**2={round(num**2,4)}\n\t{num}**3={round(num**3,4)}\n\t{num}**4={round(num**4,4)}\n\t{num}**5={round(num**5,4)}\n\t{num}**6={round(num**6,4)}\n\t{num}**7={round(num**7,4)}\n\t{num}**8={round(num**8,4)}\n\t{num}**9={round(num**9,4)}')
print(f'\n{msg}\n\t{(msg).lower()}\n\t\t{(msg).title()}\n\t\t\t{(msg).upper()}')
=======
print('!Welcome to the favorite Teacher Program!')

#Variables lista#
teacher = []
teacher.append(input('\twho is your first favorite teacher: \t').title())
teacher.append(input('\twho is your second favorite teacher: \t').title())
teacher.append(input('\twho is your third favorite teacher: \t').title())
teacher.append(input('\twho is your fourth favorite teacher: \t').title())
#imprimir lista por orden#
print(f'Your favorite teachers ranked is: {teacher}')
#imprimir lista ordenado alfabeticamente#
sorted_list = sorted(teacher)
print(f'Your favorite teacher alphabetically are: {sorted_list}')
#imprimir lista ordenada al contrario del orden alfabetico#
sorted_reverse_list = sorted(teacher,reverse = True)
print(f'Your favorite teacher in reverse order are: {sorted_reverse_list}')

#los dos favoritos#
del teacher[2:4]
print(f'Your top two favorite are: {teacher}')
#Los dos otros favoritos #
del teacher[0:1]
print(f'your other teachers favorites are: {teacher}')
print('You have 4 favorite teachers!')
#nuevo elemento#
teacher.append(input('\tOpps who is your new favorite teacher?: \t').title())
#ranked2#
print(f'Your favorite teachers ranked is: {teacher}')
#sorted2#
sorted_list = sorted(teacher)
print(f'Your favorite teacher alphabetically are: {sorted_list}')
#reverse2#
sorted_reverse_list = sorted(teacher,reverse = True)
print(f'Your favorite teacher in reverse order are: {sorted_reverse_list}')
#los dos favoritos2#
del teacher[2:4]
print(f'Your top two favorite are: {teacher}')
#Los dos otros favoritos 2#
del teacher[0:1]
print(f'your other teachers favorites are: {teacher}')
#Ultimo favorito#
del teacher[:4]
print(f'Your other teachers favorites are: {teacher}')
#numero de favoritos3
print('You have 5 teachers favorites!')




>>>>>>> 7da2e9f4f966b18fe1a907fb54b2fecb4d6b09ad
