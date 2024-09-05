for _ in range(int(input())):
    n = int(input())
    ans = n * (n+1) // 2
    pow2 = 1
    while pow2 <= n:
        ans -= pow2 * 2
        pow2 *= 2
    print(ans)
