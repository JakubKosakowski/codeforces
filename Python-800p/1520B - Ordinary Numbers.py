t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for i in range(1, 10):
        s = i
        while(s <= n):
            ans += 1
            s = s * 10 + i
    print(ans)
