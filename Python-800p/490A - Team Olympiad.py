if __name__ == "__main__":
    n = int(input())
    tab = list(map(int, input().split()))
    hash_tab = {1:[], 2:[], 3:[]}
    min_stud = []
    for i in range(len(tab)):
        hash_tab[tab[i]].append(i+1)
    if len(hash_tab[1]) == 0 or len(hash_tab[2]) == 0 or len(hash_tab[3]) == 0 or n < 3:
        print(0)
    else:
        print(min(len(hash_tab[1]), min(len(hash_tab[2]), len(hash_tab[3]))))
        for i in range(1, 4):
            min_stud = hash_tab[i] if len(hash_tab[i]) < len(min_stud) or min_stud == [] else min_stud
        for i in range(len(min_stud)):
            print(hash_tab[1][i], hash_tab[2][i], hash_tab[3][i])
