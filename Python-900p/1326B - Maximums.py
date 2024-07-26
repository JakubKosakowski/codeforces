t = int(input())
tab = list(map(int, input().split()))
max_val = 0
ans = []
i = 0
for num in tab:
   if len(ans) == 0:
      ans.append(num)
      continue
   max_val = max(max_val, ans[i])
   ans.append(num + max_val)
   i += 1
print(' '.join([str(x) for x in ans]))
