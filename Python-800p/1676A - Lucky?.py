t = int(input())
for i in range(t):
    s = input()
    num = [int(x) for x in s]
    sum_1 = sum(num[0:3])
    sum_2 = sum(num[3:])
    print("YES" if sum_1 == sum_2 else "NO")
