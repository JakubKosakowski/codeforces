for _ in range(int(input())):
    n, x, k = map(int, input().split())
    print('YES' if 2 * k >= x * (x+1) and 2 * k <= n * (n+1) - (n-x) * (n-x+1) else 'NO')
