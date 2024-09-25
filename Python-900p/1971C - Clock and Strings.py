for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    tab1 = list(range(max(a,b), 13)) + list(range(1, min(a,b)))
    tab2 = list(range(min(a,b)+1, max(a, b)))
    print('NO' if (c in tab1 and d in tab1) or (c in tab2 and d in tab2) else 'YES')
