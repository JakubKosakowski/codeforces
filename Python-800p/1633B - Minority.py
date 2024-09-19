for _ in range(int(input())):
    s = input()
    print(min((len(s) - 1) // 2, s.count('0'), s.count('1')))
