t = int(input())

months = list(map(int, input().split()))
months.sort(reverse=True)
j = 0

if t == 0:
   print(0)
else:
   while True:
      t -= months[j]
      if t <= 0:
         print(j+1)
         break
      j += 1
      if j == 12:
         print(-1)
         break
