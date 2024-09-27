n, k = map(int, input().split())
tab = list(map(int, input().split()))
ans = 1
s = sum(tab[:k])
low = s
for i in range(k, n):
    s = s - tab[i - k] + tab[i]
    if s < low:
        ans = (i - k) + 2
        low = s
print(ans)
