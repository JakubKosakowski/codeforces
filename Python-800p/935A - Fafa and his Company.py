t = int(input())
ans = 0
for i in range(1, t // 2 + 1):
    if t % i == 0:
        ans += 1
print(ans)
