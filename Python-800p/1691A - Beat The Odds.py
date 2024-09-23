for _ in range(int(input())):
    n = int(input())
    tab = list(map(int, input().split()))
    even = [x for x in tab if x % 2 == 0]
    odd = [x for x in tab if x % 2 == 1]
    print(min(len(even), len(odd)))
