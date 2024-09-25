n = int(input())
tab = list(map(int, input().split()))
i = 0
temp = 0
while True:
    temp += tab[i % 7]
    if temp >= n:
        break
    i += 1
print(i % 7 + 1)
