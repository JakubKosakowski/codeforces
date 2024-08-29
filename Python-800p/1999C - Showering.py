d = {True: "YES", False: "NO"}

for _ in range(int(input())):
    flag = False
    n, s, m = map(int, input().split())
    start = 0
    for i in range(n):
        l, r = map(int, input().split())
        if l - start >= s:
            flag = True
        start = r
    if not flag:
        flag = m - start >= s
    print(d[flag])
