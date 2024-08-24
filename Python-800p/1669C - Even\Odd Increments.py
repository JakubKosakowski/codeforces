d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    flag = True
    n = int(input())
    tab = list(map(int, input().split()))
    even = tab[0]
    odd = tab[1]
    for i in range(2, len(tab)):
        if i % 2 == 0 and tab[i] % 2 != even % 2:
            flag = False
            break
        elif i % 2 == 1 and tab[i] % 2 != odd % 2:
            flag = False
            break
    print(d[flag])
