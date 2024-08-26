t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        ans = max(ans, tab[i] * tab[i + 1])
    print(ans)
