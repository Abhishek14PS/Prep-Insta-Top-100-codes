a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
if a >= b and a >= c:
    print("greatest = " ,a)
elif b >= a and b >= c:
    print("greatest = ", b)
else:
    print("greatest = ", c)
    