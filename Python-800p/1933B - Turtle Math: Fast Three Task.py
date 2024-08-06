t = int(input())

for i in range(t):
   n = int(input())
   flag = False
   tab = list(map(int, input().split()))
   tab_sum = sum(tab)
   if tab_sum % 3 == 0:
      print(0)
      continue
   for num in tab:
      if (tab_sum - num) % 3 == 0:
         flag = True
         print(1)
         break
   if flag:
      continue
   print(3 - (tab_sum % 3))
