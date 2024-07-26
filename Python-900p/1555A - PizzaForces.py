import math

t = int(input())

for i in range(t):
   n = int(input())
   print(int(max([n + 1, 6]) // 2 * 5))
