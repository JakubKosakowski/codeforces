di = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
   r, b, d = list(map(int, input().split()))
   if r <= b:
      print(di[b <= r * (d + 1)])
   else:
      print(di[r <= b * (d + 1)])
