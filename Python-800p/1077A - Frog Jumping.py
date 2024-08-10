import math

t = int(input())

for i in range(t):
    a, b, k = list(map(int, input().split()))
    print(a * math.ceil(k / 2) - b * math.floor(k / 2))
