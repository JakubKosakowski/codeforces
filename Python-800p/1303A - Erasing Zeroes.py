t = int(input())

for i in range(t):
    flag = False
    ans = 0
    temp = 0
    s = input()
    for c in s:
        if flag:
            if c == '0':
                temp += 1
            else:
                ans += temp
                temp = 0
        else:
            if c == '1':
                flag = True
        
    print(ans)
