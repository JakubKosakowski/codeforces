t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    ans = 0
    for c in s:
        ans = max(ans, ord(c)-96)
    print(ans)
