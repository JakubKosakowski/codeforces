n = int(input())

tab = list(map(int, input().split()))

valMin = min(tab)
valMax = max(tab)
minInd = 0
maxInd = 0
result = 0

for i in range(len(tab)):
   if tab[i] == valMax:
       maxInd = i
       break

for i in range(len(tab)-1, -1, -1):
    if tab[i] == valMin:
        minInd = i
        break

result += maxInd
if maxInd > minInd:
    result += n-(minInd + 2)
else:
    result += n-(minInd + 1)

print(result)
