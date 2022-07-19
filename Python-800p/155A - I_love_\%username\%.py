n = int(input())

tab = list(map(int, input().split()))
minVal, maxVal = tab[0], tab[0]
result = 0

for i in range(1, n):
    if tab[i] > maxVal:
        maxVal = tab[i]
        result += 1
    elif tab[i] < minVal:
        minVal = tab[i]
        result += 1

print(result)
