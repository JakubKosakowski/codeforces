n, t = map(int, input().split())
temp = 10 ** (n-1)
print((temp + t - temp % t) if (temp + t - temp % t) < 10 ** n else -1)
