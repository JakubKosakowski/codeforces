n = int(input())
tab = list(map(int, input().split()))
all_c = sum(tab)
ans = 0
for num in tab:
   ans += 1 if (all_c - num) % 2 == 0 else 0
print(ans)
