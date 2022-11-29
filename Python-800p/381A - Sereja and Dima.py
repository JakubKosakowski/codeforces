t=int(input())
row = list(map(int, input().split()))
ser = 0
dim = 0
flag = True

for i in range(t):
    max = 0
    if len(row) >= 2:
        if row[0] > row[len(row)-1]:
            max = row[0]
        else:
            max = row[len(row)-1]
    else:
        max = row[0]
    row.remove(max)
    if flag:
        ser += max
        flag = False
    else:
        dim += max
        flag = True
print(str(ser) + " " + str(dim))
