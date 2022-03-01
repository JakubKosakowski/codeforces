t = int(input())

for i in range(t):
    result: int = 0
    j: int = 1
    l: str = '1'
    x = int(input())
    if x == 1:
        print(x)
    else:
        while(True):
            if l != str(x):
                if len(l) == 5:
                    j += 1
                    l = ''
                else:
                    result += len(l)
                    l += str(j)
            else:
                result += len(l)
                break
        print(result)
