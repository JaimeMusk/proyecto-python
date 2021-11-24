#saludo#
print("Welcome to the Binary/Hexadecimal Converter App")

#variable#
decimales = int(input("Compute binary and hexadecimal values up to the following decimal number:"))
N=int(input("What decimal number would you like to start at: ")) 
N1=int(input("What decimal number would you like to stop at: "))
print("Decimal values from", N, "to", N1,":")
#for#
for i in range(N,N1+1):
    print(i)
print("Binary values from",N,"to", N1 ,": ")
for x in range(N,N1+1):
    print(bin(x))
    
print("Hexadecimal values from ",N,"to", N1 ,": ")
for x in range(N,N1+1):
    print(hex(x))

#prints#
print("Press Enter to see all values from 1 to", decimales)
print("Decimal --- Binary --- Hecadecimal")
for n in range(1,decimales + 1):
    print(n,"--",bin(n),"--",hex(n))