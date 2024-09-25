a, b = map(int, input().split())
r = 0
while a >= b:
    r += b
    a -= b
    a += 1
print(a + r)
