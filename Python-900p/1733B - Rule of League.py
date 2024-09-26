for _ in range(int(input())):
    n, x, y = map(int, input().split())
    ans = []
    if x > y:
        x, y = y, x
    if x or not y or (n - 1) % y:
        print(-1)
        continue
    for k in range(2, n+1, y):
        for i in range(y):
            ans.append(str(k))
    print(' '.join(ans))
