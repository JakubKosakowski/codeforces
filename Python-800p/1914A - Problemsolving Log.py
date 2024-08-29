prblms = {}

for i in range(65, 91):
    prblms[chr(i)] = i - 64

for _ in range(int(input())):
    temp = {}
    ans = 0
    n = int(input())
    s = input()
    for c in s:
        if not c in temp:
            temp[c] = 1
        else:
            temp[c] += 1
    for key in temp.keys():
        ans += 1 if temp[key] >= prblms[key] else 0
    print(ans)
