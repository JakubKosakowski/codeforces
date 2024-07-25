ans = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
   d = {}
   temp = 0
   n, k = list(map(int, input().split()))
   s = input()
   for c in s:
      if c not in d:
         d[c] = 1
      else:
         d[c] += 1
   
   for key in d.keys():
      if d[key] % 2 == 1:
         temp += 1
   print(ans[temp <= k+1])
