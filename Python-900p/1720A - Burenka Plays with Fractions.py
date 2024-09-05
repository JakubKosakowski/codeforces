for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x, y = a * d, b * c
    if x == y:
        print('0')
    elif (y != 0 and x % y == 0) or (x != 0 and y % x == 0):
        print('1')
    else:
        print('2')
