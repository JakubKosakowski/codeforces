t = int(input())

for i in range(t):
    d = {}
    flag = True
    n = int(input())
    tab = list(map(int, input().split()))
    for num in tab:
        if not num in d:
            d[num] = 1
        else:
            d[num] += 1
            if d[num] == 3:
                print(num)
                flag = False
                break
    if flag:
        print(-1)
