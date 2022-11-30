tab = list(map(int, input().split()))
n = tab[0]
m = tab[1]
flag = True
s_flag = False
for i in range(n+1, m+1):
    for j in range(2, i):
        if i % j == 0:
            s_flag = True
            break
    if s_flag:
        s_flag = False
        continue
    else:
        flag = True if i != m else False
        break

print("YES" if not flag else "NO")
