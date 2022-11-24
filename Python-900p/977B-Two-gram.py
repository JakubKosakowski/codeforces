t = int(input())
n = input()
if len(n) == 2:
    print(n)
else:
    x = [n[i]+n[i+1] for i in range(t-1)]
    y = sorted(set(x))
    ans = ""
    temp = 0
    for d in y:
        if x.count(d) > temp:
            ans = d
            temp = x.count(d)
    print(ans)
