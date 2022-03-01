t = int(input())

for i in range(t):
    a = int(input())
    counter: int = 2
    checker: int = 2
    result: int = 1
    while(True):
        if counter <= a:
            if checker % 3 == 0 or checker % 10 == 3:
                pass
            else:
                result = checker
                counter += 1

            checker += 1
        else:
            break
    print(result)
