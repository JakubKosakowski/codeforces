n = int(input())
teams = list()
result = 0

for i in range(n):
    uniform = list(map(int, input().split()))
    teams.append(uniform)

for i in range(n):
    host = teams[i][0]
    for j in range(n):
        if host == teams[j][1]:
            result += 1

print(result)
