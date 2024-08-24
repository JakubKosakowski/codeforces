t = int(input())

for i in range(t):
    s = int(input())
    start = 9
    power = 0
    ans = 0
    temp = 0
    while s != 0:
        if s < start:
            ans += s * 10 ** power
            break
        else:
            s -= start
            ans += start * 10 ** power
            temp += start
            start -= 1
            power += 1
    print(ans)
