import math

t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        print(2)
    elif n == 2 or n == 3:
        print(1)
    else:
        print(math.ceil(n / 3))
