for _ in range(int(input())): 
    n = int(input())
    s = input()
    temp = s
    s = list(s)
    s.sort(key=lambda x: ord(x))
    print('YES' if temp == ''.join(s) else 'NO')
