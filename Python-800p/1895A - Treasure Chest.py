for _ in range(int(input())):
    x, y, k = map(int, input().split())
    print(x if y < x else y + max(0, y - x - k))
