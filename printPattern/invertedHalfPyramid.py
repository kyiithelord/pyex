# rows = 5
# num = rows
# for i in range(rows,0,-1):
#     for j in range(0,i):
#         print(num,end=' ')
#     print('\r')

rows = 5
for i in range(rows,0,-1):
    for j in range(0,i+1):
        print(j,end=' ')
    print('\    r')