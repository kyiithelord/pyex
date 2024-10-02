list1 = [5,10,15,20,25]
b_array = bytearray(list1)
print(type(b_array))
b_array[0] = 0
print(b_array[0])
for i in b_array:
    print(i,end='')
