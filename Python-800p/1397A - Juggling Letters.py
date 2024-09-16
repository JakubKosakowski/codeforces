for _ in range(int(input())):
    d = {}
    n = int(input())
    ANS = True
    for _ in range(n):
        s = input()
        for c in s:
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
    for key in d.keys():
        if d[key] % n != 0:
            ANS = False
            break
    print('YES' if ANS else 'NO')
