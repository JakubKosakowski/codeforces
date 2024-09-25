d = {}

n, m = map(int, input().split())
for i in range(m):
    first, second = input().split()
    d[first] = first if len(first) <= len(second) else second
temp = input().split()
print(' '.join([d[k] for k in temp]))
