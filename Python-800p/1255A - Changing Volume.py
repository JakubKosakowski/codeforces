t = int(input())

for i in range(t):
    tab_t = [5,2,1]
    b, a = list(map(int, input().split()))
    ans = 0
    temp = abs(b - a)
    for num in tab_t:
        ans += temp // num
        temp -= (temp // num) * num
    print(ans)
