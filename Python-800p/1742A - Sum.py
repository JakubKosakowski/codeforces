if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        tab = list(map(int, input().split()))
        if tab[0] + tab[1] == tab[2] or tab[1] + tab[2] == tab[0] or tab[0] + tab[2] == tab[1]:
            print("YES")
        else:
            print("NO")
