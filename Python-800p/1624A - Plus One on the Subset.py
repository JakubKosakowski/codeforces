t = int(input())
for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    print(max(tab)-min(tab))
