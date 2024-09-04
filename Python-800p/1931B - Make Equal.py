for _ in range(int(input())):
    n = int(input())
    flag = False
    tab = list(map(int, input().split()))
    k = sum(tab) // n
    for i in range(n - 1):
        if tab[i] < k:
            print('NO')
            flag = True
            break
        tab[i+1] += tab[i] - k
        tab[i] = k
    if flag:
        continue
    print('YES')
