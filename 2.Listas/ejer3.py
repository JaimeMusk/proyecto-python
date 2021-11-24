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