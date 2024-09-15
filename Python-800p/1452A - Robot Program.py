for _ in range(int(input())):
    x, y = map(int, input().split())
    if abs(x - y) <= 1:
        print(x + y)
        continue
    else:
        print(max(x, y) * 2 - 1)
