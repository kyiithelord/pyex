number1 = int(input("Enter Your First Number : "))
number2 = int(input("Enter Your Second Number : "))
if number1 >= number2:
    if number1 == number2:
        print("Number1 and Number2 are equal")
    else:
        print("Number1 is greater than Number2")
else:
    print("Number1 is smaller than Number2")