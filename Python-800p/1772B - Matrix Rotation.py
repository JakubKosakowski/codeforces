d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
   col_1 = list(map(int, input().split()))
   col_2 = list(map(int, input().split()))
   temp = col_1 + col_2
   min_v = min(temp)
   max_v = max(temp)
   print(d[temp.index(min_v) + temp.index(max_v) == 3])
