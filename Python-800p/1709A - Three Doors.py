d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    x = int(input())
    tab = list(map(int, input().split()))
    print(d[tab[x-1] != 0 and tab[tab[x-1] - 1] != 0])
