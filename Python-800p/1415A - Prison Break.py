t = int(input())

for i in range(t):
    n, m, r, c = list(map(int, input().split()))
    print(max([abs(1 - r) + abs(1 - c),
               abs(n - r) + abs(m - c),
               abs(1 - r) + abs(m - c),
               abs(n - r) + abs(1 - c)]))
