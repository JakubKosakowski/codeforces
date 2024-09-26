n, m = map(int, input().split())
t = list(map(int, input().split()))
start = 1
ans = 0
for c in t:
    if c >= start:
        ans += c - start
    else:
        ans += n - start + c
    start = c
print(ans)
