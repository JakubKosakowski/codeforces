for _ in range(int(input())): 
    n, k = map(int, input().split())
    tab = list(map(int, input().split()))
    ans = 0
    temp = 0
    for num in tab:
        if num >= k:
            temp += num
        elif num == 0 and temp != 0:
            ans += 1
            temp -= 1
    print(ans)
