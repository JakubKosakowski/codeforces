d = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

t = int(input())

for i in range(t):
    ans = ''
    n = int(input())
    s = input()
    j = 0
    if n == 1:
        print(d[s])
        continue
    else:
        while j < n:
            if d[s[j+1]] == s[j]:
                ans += f'{s[j]}{s[j+1]}'
                j += 2
            else:
                ans += f'{d[s[j]]}'
                j += 1

            if j == n - 1:
                ans += f'{d[s[j]]}'
                break
    print(ans)
    
