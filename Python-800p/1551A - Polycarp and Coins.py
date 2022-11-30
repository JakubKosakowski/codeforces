t = int(input())
for i in range(t):
    x = int(input())
    a = x // 3
    b = a
    if x - (a * 2 + b) == 1:
        b = a + 1
    elif x - (a * 2 + b) == 2:
        a += 1
    print(str(b) + " " + str(a))
