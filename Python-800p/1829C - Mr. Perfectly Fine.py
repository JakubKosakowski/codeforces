for _ in range(int(input())):
    n = int(input())
    first = -1
    second = -1
    both = 0
    for _ in range(n):
        value, s = input().split()
        value = int(value)
        if s == '11':
            both = min(both, value) if both != 0 else value
        elif s == '01':
            second = min(second, value) if second != -1 else value
        elif s == '10':
            first = min(first, value) if first != -1 else value
    if (first == -1 or second == -1):
        print(-1 if both == 0 else both)
    else:
        print(min(first + second, both) if both != 0 else first + second)
