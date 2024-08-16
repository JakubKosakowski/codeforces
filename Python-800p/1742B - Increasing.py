d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    print(d[len(set(tab)) == len(tab)])
