d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    a,b,c = list(map(int, input().split()))
    print(d[a + b >= 10 or a + c >= 10 or b + c >= 10])
