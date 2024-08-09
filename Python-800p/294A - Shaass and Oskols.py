n = int(input())
wires = list(map(int, input().split()))
m = int(input())

for i in range(m):
   x, y = list(map(int, input().split()))
   temp = wires[x-1]
   wires[x-1] = 0
   if x != 1:
      wires[x-2] += y-1
   if x != n:
      wires[x] += temp - y

print('\n'.join([str(x) for x in wires]))
