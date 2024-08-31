d = [0, 0, 0]
list_exer = ['chest', 'biceps', 'back']
n = int(input())
exer = map(int, input().split())
for ind, e in enumerate(exer):
    d[ind % 3] += e
print(list_exer[d.index(max(d))])
