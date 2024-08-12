n, x = list(map(int, input().split()))
tab = list(map(int, input().split()))
temp = abs(sum(tab))
if temp % x == 0:
    print(temp // x)
else:
    print(temp // x + 1)
