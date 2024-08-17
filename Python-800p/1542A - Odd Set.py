d = {True: 'Yes', False: 'No'}

t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    even = [x for x in tab if x % 2 == 0]
    odd = [x for x in tab if x % 2 == 1]
    print(d[len(odd) == len(even)])
