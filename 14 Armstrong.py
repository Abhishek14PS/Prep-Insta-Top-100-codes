n = int(input("enter a number: "))
original = n
n_digit = len(str(n))
sum = 0 
while n > 0:
    digit = n % 10
    sum += digit ** n_digit
    n //= 10
if sum == original:
    print("Yes")
else:
    print("No")