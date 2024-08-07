n = int(input())
tab = list(map(int, input().split()))

d = abs(tab[0] - tab[n-1])
m = min([1001, d])

ind_1, ind_2 = (1, n)

for i in range(n-1):
   d = abs(tab[i] - tab[i+1])
   if m > d:
      m = d
      ind_1 = i + 1
      ind_2 = i + 2

print(ind_1, ind_2)
