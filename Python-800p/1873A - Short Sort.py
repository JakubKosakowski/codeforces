d = {True: "YES", False: 'NO'}

t = int(input())

for i in range(t):
    s = input()
    print(d[s[0] == 'a' or s[1] == 'b' or s[2] == 'c'])
