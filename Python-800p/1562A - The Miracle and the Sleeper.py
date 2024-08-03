import math

t = int(input())

for i in range(t):
   l, r = list(map(int, input().split()))
   if r // 2 < l:
      print(r % l)
      continue
   if r % 2 == 0:
      print((r-1) % math.ceil(r / 2))
   else:
      print(r % math.ceil(r / 2))
