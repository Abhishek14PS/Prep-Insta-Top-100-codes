num = int(input("enter a number: "))
n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()