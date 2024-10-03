start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
for number in range(start, end + 1):
    if number <= 1:
        continue  
    is_prime = True
    if number == 2:
        print(number) 
    elif number % 2 == 0:
        continue 
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)