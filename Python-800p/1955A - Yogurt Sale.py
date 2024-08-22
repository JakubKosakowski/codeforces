t = int(input())

for i in range(t):
    n, a, b = list(map(int, input().split()))
    print(min((n // 2) * b + (n % 2) * a, n * a))
