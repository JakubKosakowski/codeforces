t = int(input())

for i in range(t):
    d = {}
    for j in range(3):
        row = input()
        for c in row:
            if c != '?':
                d[c] = 1 if not c in d else d[c] + 1
    for key in d.keys():
            if d[key] == 2:
                print(key)
                break
