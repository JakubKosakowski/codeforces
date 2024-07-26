t = int(input())

for i in range(t):
   x, n = list(map(int, input().split()))
   temp = {0: 0, 1: -n, 2: 1}
   ans = temp[n % 4] if n % 4 != 3 else n + 1
   if x == 0:
      print(ans)
   elif x % 2 == 0:
      print(x + ans)
   else:
      print(x - ans)
