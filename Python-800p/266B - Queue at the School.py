tab = list(map(int, input().split()))
n = tab[0]
t = tab[1]

a = list(input())
d = ""

while (t>0):
    i=0
    while i<(len(a)-1):
        if(a[i]=='B' and a[i+1]=='G'):
            a[i], a[i+1] = a[i+1], a[i]
            i += 1
        i += 1
    t -= 1

for element in a:
    d += element

print(d)
