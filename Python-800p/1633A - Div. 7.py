t = int(input())

for i in range(t):
   n = int(input())
   if n % 7 == 0:
      print(n)
      continue
   n = (n // 10) * 10
   for i in range(10):
      if (n + i) % 7 == 0:
         print(n + i)
         break
