t = int(input())
ans = 0
temp = 0
tab = []
if t == 2:
    print(1)
    print(2)
elif t == 3:
    print(1)
    print(3)
else:
    while(True):
        ans += 1
        temp += 2
        tab.append(2)
        if temp == t:
            break
        elif t - temp == 3:
            ans += 1
            temp += 3
            tab.append(3)
            break
    print(ans)
    print(" ".join(str(x) for x in tab))
