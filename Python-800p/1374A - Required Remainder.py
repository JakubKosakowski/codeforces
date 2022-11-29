t = int(input())
for i in range(t):
    tab = list(map(int, input().split()))
    x = tab[0]
    y = tab[1]
    n = tab[2]
    if n % x == y:
        print(n)
    elif n % x > y:
        print(n - (n % x) + y)
    else:
        print(n - ((n % x) + (x - y)))
