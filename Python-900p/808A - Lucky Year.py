import math

t = int(input())

st = str(t)
p = 10 ** (len(st) - 1)

if t <= 9:
    print(1)
elif t % p == 0:
   print(p)
else:
   print(math.ceil(t / p) * p - t)    
