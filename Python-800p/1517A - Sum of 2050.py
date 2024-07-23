t = int(input())

for i in range(t):
   num = int(input())
   if num % 2050 != 0:
      print(-1)
      continue
   temp = str(num // 2050)
   print(sum([int(x) for x in temp]))
