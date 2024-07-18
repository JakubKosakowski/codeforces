d = {True: '+', False: '-'}

t = int(input())

for i in range(t):
    a,b,c = list(map(int, input().split()))
    print(d[a+b == c])
