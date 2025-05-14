input_str = input("\nVui lòng nhập X,Y : ")
kich_thuoc = [int(x) for x in input_str.split(',')]

hangNum = kich_thuoc[0]
cotNum = kich_thuoc[1]

multilist = [[0 for col in range(cotNum)] for row in range(hangNum)]
for row in range(hangNum):
    for col in range(cotNum):
        multilist[row][col] = row*col
print (multilist)