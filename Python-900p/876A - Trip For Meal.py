n = int(input())
a = int(input())
b = int(input())
c = int(input())
if n == 1 or min([a,b,c]) in [a,b]:
    print(min(a,b)*(n-1))
else:
    print(min(a,b) + c * (n-2))
