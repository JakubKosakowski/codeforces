import math

for _ in range(int(input())): 
    n = int(input())
    t = list(map(int, input().split()))
    temp = set(t)
    ans = 0
    for m in temp:
        ans += math.ceil(t.count(m) * m / 2) if m in [1, 2] else t.count(m)
    print(ans)
