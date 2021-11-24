

#import + funcion#
import uuid
def print_shipping_prices():
    print('\n Current Shipping price are : ')
    print('\Shipping orders 0 to 100: \t\t $5.10 each')
    print('\nShipping orders 100 to 500: \t\t $5.00 each')
    print('\nShipping orders 500 to 1000: \t\t $4.95 each')
    print('\nShipping orders over 1000: \t\t $4.80 each')


#funcion2 + if#
def print_quotation(items:int):
    if items > 0 and items <= 100:
        print(f'\tTo ship {items} items will cost you ${round(5.10 * items,2)}, at $5.10 per item.')
    elif items > 100 and items <=500:
        print(f'\tTo ship {items} items will cost you ${round(5.00 * items,2)}, at $5.00 per item.')
    elif items > 500 and items <= 1000:
        print(f'\t To ship {items} items will cost you ${round(4.95 * items,2)}, at $4.95 per item.')
    elif items > 1000: 
        print(f'\tTo ship {items} items will cost you ${round(4.80 * items,2)}, at $4.80 per item.')

#saludo#
print(f'\tWelcome to the Shipping account program.')
#lista#

user_list = ['Jaime', 'Bosco', 'Lucas', 'Rakel', 'Luis']

name=input('\tHellowtha, Enter your name : ').title().strip()
#condicional de la lista#
if name in user_list:
    print(f'\n Welcome {name}')
    print_shipping_prices()
    items_to_be_shipped = int(input('\tHow many items do you want to ship : '))
    print_quotation(items_to_be_shipped)
    place_order = input('\tWould you like to place the order ? [Y/N} ').lower()
    if place_order == 'y':
        print(f'\tOrder placed for {items_to_be_shipped} items. Your orderid #{uuid.uuid1()}.\n Thank you !')
    elif place_order == 'n':
        print(f'\t Order not placed.\n Thank you !')
    else:
        print('\t Error system')

else:
    print('\t Sorry, you do not have an account with us. Goodbye.')  