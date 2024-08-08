t = int(input())

for i in range(t):
   n = int(input())
   tab = list(map(int, input().split()))
   temp = []
   for i in range(len(tab) - 1):
      temp.append(max(tab[i], tab[i+1]))
   print(min(temp) - 1)
