tab = list(map(int, input().split()))
n = tab[0]
k = tab[1]
aot = 240 - k
check = 0
result = 0

for i in range(n):
    check += 5 * (i+1)
    if check <= aot:
        result += 1
    else:
        break

print(result)
