for _ in range(int(input())):
    n = int(input())
    tab = list(map(int, input().split()))
    first = tab.index(1)
    last = tab[::-1].index(1)
    print(tab[first:len(tab)-last].count(0))
