t = int(input())
temp = 'codeforces'

for i in range(t):
    ans = 0
    word = input()
    for i, c in enumerate(word):
        ans += 1 if temp[i] != c else 0
    print(ans)
