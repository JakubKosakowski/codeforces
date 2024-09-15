for _ in range(int(input())):
    n = int(input())
    tab = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        for j in range(i):
            if abs(tab[i] - tab[j]) == 1:
                ans = 0
                break
        if not ans:
            break
    print(2 - ans)
