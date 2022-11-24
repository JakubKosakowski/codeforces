import math

t = int(input())
for i in range(t):
    tab = list(map(int, input().split()))
    h = tab[0]
    v = tab[1]
    l = tab[2]
    if h - l*10 <= 0:
        print("YES")
    else:
        for i in range(v):
            h = math.floor(h/2) + 10
        if h - l*10 <= 0:
            print("YES")
        else:
            print("NO")
