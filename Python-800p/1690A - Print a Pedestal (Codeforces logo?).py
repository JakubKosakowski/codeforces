for _ in range(int(input())):
    n = int(input())
    h1, h2, h3 = 3, 2, 1
    for i in range(7, n+1):
        if i % 3 == 0:
            h3 += 1
        elif i % 3 == 1:
            h1 += 1
        else:
            h2 += 1
    print(h2, h1, h3)
