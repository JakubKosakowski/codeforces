d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
   n = int(input())
   y = n % 2020
   x = (n - y) / 2020 - y
   print(d[x >= 0])
