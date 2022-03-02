n = int(input())

for i in range(n):
    s = int(input())
    line = list(map(int, input().split()))
    line.sort()
    result: int = 0
    for j in range(1,len(line)):
        if j == 1:
            result = abs(line[j-1] - line[j])
        else:
            if abs(line[j-1] - line[j]) < result:
                result = abs(line[j - 1] - line[j])
    print(result)
