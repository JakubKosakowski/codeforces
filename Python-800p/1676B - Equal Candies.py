t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    m = min(tab)
    ans = 0
    for num in tab:
        ans += num - m
    print(ans)
