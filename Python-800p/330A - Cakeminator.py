t = input()
a = tuple(int(x) for x in t.split())
val: list = list()
row: list = list()
col: list = list()

for i in range(a[0]):
    l = list(map(str, input()))
    val.append(l)

for i in range(len(val)):
    for j in range(len(val[i])):
        if val[i][j] == 'S':
            row.append(i)
            col.append(j)

row.sort()
col.sort()
result: int = 0
check: int = 0
for i in range(a[0]):
    if i not in row:
        result += a[1]
        check += 1

for i in range(a[1]):
    if i not in col:
        result += (a[0]- check)

print(result)


