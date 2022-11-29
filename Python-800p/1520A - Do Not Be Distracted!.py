t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    let = set(s)
    tab = list()
    for j in let:
        flag = False
        app = 0
        for k in s:
            if j == k:
                if not flag:
                    flag = True
                    app += 1
            else:
                if flag:
                    flag = False
        tab.append(app)
    cor = True
    for j in tab:
        if j != 1:
            print("NO")
            cor = False
            break
    if cor:
        print("YES")
