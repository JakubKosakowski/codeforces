t = int(input())

for i in range(t):
   n = int(input())
   t = list(map(int, input().split()))
   if sum(t) % 2 != 0:
      print('NO')
   else:
      temp = (t.count(1) + t.count(2) * 2) / 2
      if temp % 2 == 0 or (temp % 2 == 1 and t.count(1) != 0):
         print('YES')
      else:
         print('NO')
