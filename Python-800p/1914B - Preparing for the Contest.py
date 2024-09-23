for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = [str(x) for x in range(n-k, n+1)] + [str(x) for x in range(n-k-1, 0, -1)]
    print(' '.join(ans))
