n = int(input())

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        print(int(x/2))
    else:
        print(int((x+1)/2))
