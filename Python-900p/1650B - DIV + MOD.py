t = int(input())
for i in range(t):
    tab = list(map(int, input().split()))
    l = tab[0]
    r = tab[1]
    a = tab[2]
    ans = r // a + r % a
    m = r // a * a - 1
    if m >= l:
        ans = max(ans, m // a + m % a)
    print(ans)
