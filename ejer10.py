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




