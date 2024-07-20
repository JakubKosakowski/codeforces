d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    flag = True
    l = int(input())
    r1 = input()
    r2 = input()
    for i, c in enumerate(r1):
        if (c in ('G', 'B') and r2[i] not in ('G', 'B')) or (c == 'R' and r2[i] != 'R'):
            flag = False
            break
    print(d[flag])
