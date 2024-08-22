d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    print(d[sum([x for x in tab if x % 2 == 0]) > sum([x for x in tab if x % 2 == 1])])
