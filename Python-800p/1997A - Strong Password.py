for _ in range(int(input())): 
    s = input()
    s = list(s)
    flag = True
    temp = ''
    for i, c in enumerate(s):
        if temp == c:
            s.insert(i, chr(97 + abs(97 - ord(c) + 1)))
            flag = False
            break
        temp = c
    if flag:
        s.append(chr(97 + abs(97 - ord(s[-1]) + 1)))
    print(''.join(s))
