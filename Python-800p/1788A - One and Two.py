t = int(input())

for i in range(t):
   n = int(input())
   tab = list(map(int, input().split()))
   twos = tab.count(2)
   half = twos // 2
   i = 0
   ans = 0
   if twos % 2 == 1:
      print(-1)
      continue
   if tab.count(1) == n:
      print(1)
      continue
   while twos > half:
      if tab[i] == 2:
         twos -= 1
      i += 1
      ans += 1
   print(ans)
