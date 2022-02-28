from decimal import *
n = int(input())
m = list(map(int, input().split()))
print(Decimal(sum(m))/Decimal(len(m)))
