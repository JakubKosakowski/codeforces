temp = ['h', 'e', 'l', 'l', 'o']
ind = 0
s = input()
for c in s:
    if ind == 5:
        break
    if c == temp[ind]:
        ind += 1
print('YES' if ind == 5 else 'NO')
