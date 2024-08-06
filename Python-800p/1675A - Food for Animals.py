d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
   a, b, c, x, y = list(map(int, input().split()))
   if x > a + c or y > b + c:
      print('NO')
      continue
   c = (c + a) - x
   print(d[y <= b + c])
