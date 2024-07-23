d = {0: 'NONE', 1: 'PEAK', 2: 'STAIR'}

t = int(input())

for i in range(t):
   a, b, c = list(map(int, input().split()))
   if a < b and b < c:
      print('STAIR')
   elif a < b and b > c:
      print('PEAK')
   else:
      print('NONE')
