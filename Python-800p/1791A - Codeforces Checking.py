d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
    c = input()
    print(d[c in 'codeforces'])
