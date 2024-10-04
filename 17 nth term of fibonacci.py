n = int(input("Enter the term position (N): "))
if n <= 0:
    print("The term should be a positive integer.")
elif n == 1:
    print(f"The {n}th Fibonacci term is 0")
elif n == 2:
    print(f"The {n}th Fibonacci term is 1")
else:
    n1 = int(input("Enter a number : "))
    n2 = int(input("Enter a number: "))
    for i in range(2, n):
        nth = n1 + n2
        n1, n2 = n2, nth  
    print(f"The {n}th Fibonacci term is {nth}")