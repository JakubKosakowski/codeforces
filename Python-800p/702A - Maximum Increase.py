n = int(input())
tab = list(map(int, input().split()))
ans = 0
prev = 0
temp = 0

for num in tab:
    if num > prev:
        temp += 1
    else:
        ans = max(ans, temp)
        temp = 1
    prev = num
ans = max(ans, temp)
print(ans)
