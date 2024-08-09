n, k = list(map(int, input().split()))
tab = list(map(int, input().split()))
flag = False
ans = 0

for num in tab:
   if num <= k:
      ans += 1
   else:
      break

if ans == n:
   print(n)
else:
   for num in tab[::-1]:
      if num <= k:
         ans += 1
      else:
         break

   print(ans) 
