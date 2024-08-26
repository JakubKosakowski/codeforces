t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))
    print(min(min(a,b), (a+b) // 4))
