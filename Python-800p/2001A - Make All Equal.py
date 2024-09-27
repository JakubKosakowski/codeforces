for _ in range(int(input())): 
    n = int(input())
    t = list(map(int, input().split()))
    temp = set(t)
    ans = 0
    for m in temp:
        ans = max(ans, t.count(m))
    print(len(t) - ans)
