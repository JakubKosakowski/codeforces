n = int(input())
tab = list(map(int, input().split()))
min_val = min(tab)
max_val = max(tab)
ans = 0
for i in range(n):
    ans += 1 if min_val < tab[i] and tab[i] < max_val else 0
print(ans)
