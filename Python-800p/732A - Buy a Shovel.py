tab = list(map(int, input().split()))

ans = 1

while True:
    if (tab[0] * ans - tab[1]) % 10 == 0 or (tab[0] * ans) % 10 == 0:
        break
    ans += 1

print(ans)
