def multi(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * multi(arr[1:])

t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    tab[tab.index(min(tab))] += 1
    print(multi(tab))
