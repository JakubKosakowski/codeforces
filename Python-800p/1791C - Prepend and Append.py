t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    ans = 0
    for i in range(len(s) // 2 + 1):
        if not (int(s[i]), int(s[-i - 1])) in [(1,0), (0, 1)]:
            ans = len(s[i:len(s)-i])
            break
    print(ans)
