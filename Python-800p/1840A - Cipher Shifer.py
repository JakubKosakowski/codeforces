for _ in range(int(input())):
    n = int(input())
    a = input()
    ans = ''
    l = ''
    for c in a:
        if l == '':
            l = c
        elif l == c:
            ans += l
            l = ''
    print(ans)
