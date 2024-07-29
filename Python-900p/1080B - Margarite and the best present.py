def F(x):
   if(x % 2 == 0):
      return x // 2
   else:
      return -x + F(x-1)

t = int(input())
for i in range(t):
   l, r = list(map(int, input().split()))
   print(F(r) - F(l-1))
