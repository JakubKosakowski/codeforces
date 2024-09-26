s, n = map(int, input().split())
dragons = []
ans = True
for i in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))
dragons.sort()
while True:
    flag = False
    for t in dragons:
        if s > t[0]:
            s += t[1]
            flag = True
            dragons.remove(t)
            break
    if len(dragons) == 0:
        break
    if not flag:
        ans = False
        break
print('YES' if ans else 'NO')
