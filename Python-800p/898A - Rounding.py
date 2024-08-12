n = int(input())

ans = n - (n % 10) if n % 10 <= 5 else n + (10 - n % 10)
print(ans)
