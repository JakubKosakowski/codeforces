t = int(input())

tab = list()

for i in range(t):
    a = input()
    result = str()
    for i in range(0, len(a)-1, 2):
        result += a[i]
    result += a[-1]
    tab.append(result)

for i in range(len(tab)):
    print(tab[i])
