d = {True: 'First', False: 'Second'}

t = int(input())

for i in range(t):
    n = int(input())
    print(d[(n+1) % 3 == 0 or (n-1) % 3 == 0])
