d = {0: 0, 1: 0, 2: 0}

for _ in range(int(input())):
    vec = list(map(int, input().split()))
    d[0] += vec[0]
    d[1] += vec[1]
    d[2] += vec[2]
print('YES' if list(d.values()) == [0, 0, 0] else 'NO')
