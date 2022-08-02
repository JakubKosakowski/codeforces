t = int(input())

for i in range(t):

    sum1, sum2 = 0, 0

    n = int(input())
    if n % 4 != 0:
        print("NO")
    else:
        print("YES")
        tab = list()
        for i in range(2, n+1, 2):
            print(str(i) + " ")
            sum1 += i
        for i in range(1, n-2, 2):
            print(str(i) + " ")
            sum2 += i
        print(sum1 - sum2)
