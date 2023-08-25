if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        tab = list(map(int, input().split()))
        tab.sort()
        print(tab[1]) 
