import math

d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    b = int(input())
    s = list(map(int, input().split()))
    all = sum(s)
    print(d[math.sqrt(all) % math.floor(math.sqrt(all)) == 0])
