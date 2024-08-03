import math

t = int(input())

for i in range(t):
   a, b, c = list(map(int, input().split()))
   if b % 3 != 0 and (b + c) % 3 != 0 and (b % 3) + c < 3:
      print(-1)
      continue
   print(a + math.ceil((b + c) / 3))
