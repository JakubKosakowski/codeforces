for _ in range(int(input())):
    n = int(input())
    s = input()
    temp = 0
    for c in s:
        temp += 1 if c == '(' else 0
        temp -= 1 if c == ')' and temp != 0 else 0
    print(temp)
