for i in range(0,10):
    currentNumber = i
    previousNumber = i -1
    if i == 0:
        previousNumber = -1
    totalNumber = previousNumber + currentNumber
    print('the current number is :',i,"previous number is :",previousNumber,'the total number is :',totalNumber)
