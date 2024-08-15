t = int(input())

for i in range(t):
    d = {}
    n = int(input())
    s = input()
    ans = 0
    for c in s:
        if not c in d:
            d[c] = True
            ans += 2
        else:
            ans += 1
    print(ans)
