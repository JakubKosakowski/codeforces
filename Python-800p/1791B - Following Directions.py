d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    flag = False
    n = int(input())
    s = input()
    x, y = 0, 0
    for c in s:
        if c in ['U', 'D']:
            y += 1 if c == 'U' else -1
        else:
            x += 1 if c == 'R' else -1
        if (x, y) == (1, 1):
            flag = True
            break
    print(d[flag])
