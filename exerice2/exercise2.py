for i in range(0,10):
    currentNumber = i
    previousNumber = i - 1
    if i == 0:
        previousNumber = 0
    totalNumber = previousNumber + currentNumber
    print("current Number is : ",currentNumber,"PreviousNumber is : ",previousNumber, "total Numberis ",totalNumber)