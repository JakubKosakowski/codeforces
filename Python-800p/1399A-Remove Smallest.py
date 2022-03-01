t = int(input())

for i in range(t):
    n = int(input())
    checker: int = 0
    line = list(map(int, input().split()))
    line.sort()
    if(n == 1):
        print("YES")
    else:
        for j in range(1,len(line)):
            if(abs(line[j-1] - line[j]) > 1):
                print("NO")
                break
            else:
                checker += 1
                if checker == len(line)-1:
                    print("YES")
                    break
