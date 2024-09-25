n = int(input())
flag = False
temp = ''
temp_set = set()
for i in range(n):
    row = input()
    if temp == '':
        temp = row[0]
    temp_set.update(set(row))
    if (row.count(temp) != 2 and i != n // 2) or (row.count(temp) != 1 and i == n //2):
        flag = True
print('NO' if flag or len(temp_set) != 2 else 'YES')
