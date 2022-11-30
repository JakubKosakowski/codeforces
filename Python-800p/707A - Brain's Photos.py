sizes = list(map(int, input().split()))
n = sizes[0]
m = sizes[1]
flag = False
for i in range(n):
    tab = list(map(str, input().split()))
    if 'C' in tab or 'M' in tab or 'Y' in tab:
        flag = True
if flag:
    print("#Color")
else:
    print("#Black&White")
