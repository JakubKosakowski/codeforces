tab, e = list(map(int, input().split())), 3
tab.sort()

for i in range(3):
    if tab[i] != tab[i + 1]:
        e -= 1

print(e)
