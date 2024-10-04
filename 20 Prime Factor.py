num = int(input("Enter a number: "))
divisor = 2
while num > 1:
    while num % divisor == 0:
        print(divisor, end=" ")
        num //= divisor
    divisor += 1