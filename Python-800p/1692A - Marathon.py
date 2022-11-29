t = int(input())
for i in range(t):
    tab = list(map(int, input().split()))
    sor = sorted(tab)
    for j in range(len(tab)):
        if tab[0] == sor[j]:
            print(len(tab) - 1 - j)
