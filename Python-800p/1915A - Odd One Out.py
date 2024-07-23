t = int(input())

for i in range(t):
   temp = {}
   tab = list(map(int, input().split()))
   for n in tab:
      if n not in temp:
         temp[n] = 1
      else:
         del temp[n]
   print(list(temp.keys())[0])
