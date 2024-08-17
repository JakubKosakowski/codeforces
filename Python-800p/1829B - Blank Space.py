t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    temp = 0
    ans = 0
    for num in tab:
        if num == 0:
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 0
    ans = max(ans, temp)
    print(ans)
