a = int(input("enter a number: "))
b = int(input("enter a number: "))
for i in range(a,b+1):
    num_digit = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digit
        temp //= 10
    if sum == i:
        print(i)