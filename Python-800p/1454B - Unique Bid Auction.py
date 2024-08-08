t = int(input())

for i in range(t):
   d = {}
   flag = False
   n = int(input())
   min_val = n + 1
   tab = list(map(int, input().split()))
   for num in tab:
      if not num in d:
         d[num] = True
      else:
         d[num] = False
   for key in d.keys():
      if d[key]:
         flag = True
         min_val = key if key < min_val else min_val
   if not flag:
      print(-1)
      continue
   print(tab.index(min_val) + 1)
