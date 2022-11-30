t = int(input())
for i in range(t):
    tab = list(map(int, input().split()))
    max_val = max(tab[:3])
    temp = 0
    for x in tab[:3]:
        temp += (max_val - x)
    print("NO" if temp > tab[3] or (tab[3] - temp) % 3 != 0 else "YES")
