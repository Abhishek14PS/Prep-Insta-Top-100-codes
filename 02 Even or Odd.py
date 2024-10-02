a = int(input("Enter a number: "))
if a > 0:
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
elif a < 0:
    print("negative")
else:
    print("zero")