tab = list(map(int, input().split()))
tab_val = list(map(int, input().split()))

result = 0

for element in tab_val:
    if element + tab[1] <= 5:
        result += 1

print(int(result/3))
