#saludo#

print('\n Welcome to the Fibonacci app.')
#variable#
number = int(input('\n Enter the number of digits you want to compute Fibonacci : '))

fib_list = [1,1]

for i in range (number-2):
    new_fib = fib_list[i] + fib_list[i+1]
    fib_list.append(new_fib) #.append para listas

print(f'\n The Fibonacci sequence for {number} : ')
for i in fib_list:
    print(f'\n{i}')

#lista golden#
golden_list = list(fib_list)

for i in range(len(fib_list)-1):
    golden_ratio = fib_list[i+1]/fib_list[i]
    golden_list.append(golden_ratio)
#resultado de la seccuencia #
print(f'\n The corresponding golden ratio sequence for {number} : ')
for i in golden_list:
    print(f'\n{i}')
