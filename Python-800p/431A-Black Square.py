line = list(map(int, input().split()))
cals = input()

cals = list(cals)
result: int = 0

for cal in cals:
    result += int(line[int(cal)-1])

print(result)
