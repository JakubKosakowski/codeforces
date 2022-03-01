n: int = 0

matrix: list = list()
row: int = 0
col: int = 0

while n < 5:
    line = list(map(int, input().split()))
    matrix.append(line)
    n += 1

for line in matrix:
    if 1 in line:
        col = line.index(1)
        break
    else:
        row += 1

print(abs(2-row) + abs(2-col))
