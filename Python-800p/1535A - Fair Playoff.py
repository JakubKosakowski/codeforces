d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    com = list(map(int, input().split()))
    w1 = max(com[:2])
    w2 = max(com[2:])
    temp = [w1, w2]
    com.sort()
    temp.sort()
    print(d[temp == com[2:]])
