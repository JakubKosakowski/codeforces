t = int(input())

for i in range(t):
    max_v = 0
    ans = 0
    n = int(input())
    for j in range(n):
        a, b = list(map(int, input().split()))
        if a <= 10 and b > max_v:
            max_v = b
            ans = j+1
    print(ans)
