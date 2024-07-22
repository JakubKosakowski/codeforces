t = int(input())

temp = [x for x in '1234567890']

for i in range(t):
    ans = 0
    s = input()
    dest = 0
    for c in s:
       ans += abs(dest - temp.index(c)) + 1
       dest = temp.index(c) 
    print(ans)
