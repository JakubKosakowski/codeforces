for _ in range(int(input())): 
    n = int(input())
    g_t = 0
    l_t = -1
    n_e = set()
    ans = 0
    for i in range(n):
        a, x = map(int, input().split())
        if a == 1:
            g_t = max(g_t, x)
        elif a == 2:
            l_t = min(l_t, x) if l_t != -1 else x
        else:
            n_e.add(x)
    if l_t < g_t:
        print(0)
        continue
    ans = l_t - g_t + 1
    for c in n_e:
        ans -= 1 if g_t <= c and c <= l_t else 0
    print(ans)
