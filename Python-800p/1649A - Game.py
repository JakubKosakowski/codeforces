t = int(input())

for i in range(t):
    n = int(input())
    tab = list(map(int, input().split()))
    if tab.count(0) == 0:
        print(0)
        continue
    first_zero = tab.index(0)
    last_zero = len(tab) - tab[::-1].index(0) + 1
    print(last_zero - first_zero)
