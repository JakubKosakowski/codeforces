for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in range(n):
        ans.append(str(i*2+1))
    print(' '.join(ans))
