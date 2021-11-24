<<<<<<< HEAD
print('welcome to the Temperature Conversation App)
fah = input('what is the  given Temperature in degress Fahrenheit?: ')
degress = float(input(fah)
celsius = float(input((fah-32)*(5/9))
kelvin = float(input((celsius+273))
=======
##Saludo##
print('Welcome to the  Grocery List App')

##variables##
import datetime
compra = ("meat", "cheese")
print("welcome!")
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
print("current date ant time:", day,"/",month,"/  ",hour,":",minute)
print("products in your list: meat and cheese")

p1 = input("introduce another product: ")
p2 = input("introduce another product: ")
p3 = input("introduce another product: ")
##compra##
compra = ["meat","cheese",p1,p2,p3]
print("your actual list is :",compra, "and sorted:",sorted(compra))
print("current grocery list:", len(compra),"items")
>>>>>>> 7da2e9f4f966b18fe1a907fb54b2fecb4d6b09ad
