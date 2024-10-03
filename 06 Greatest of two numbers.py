a = int(input("enter a number: "))
b = int(input("enter a number: "))
if a > 0:
    if a == b:
        print("equal")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is smaller than b")
else:
    print("negative number")