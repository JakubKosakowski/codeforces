import math

t = int(input())
for i in range(t):
    n  = int(input())
    tab = list(map(int, input().split()))
    ans = 0
    odd = 0
    even = 0
    for j in range(n):
        if tab[j] % 2 == 0:
            even += 1
        else:
            odd += 1
    if (n % 2 == 1 and odd != math.floor(len(tab)/2)) or (n % 2 == 0 and even != len(tab)//2) or (n == 1 and tab[0] % 2 == 1):
        print(-1)
    elif(n == 1 and tab[0] % 2 == 0):
        print(0)
    else:
            odd_cor = 0
            even_cor = 0
            for k in range(n):
                if k % 2 == 0 and tab[k] % 2 == 0:
                    even_cor += 1
                elif k % 2 == 1 and tab[k] % 2 == 1:
                    odd_cor += 1
            print(max(odd - odd_cor, even - even_cor))
