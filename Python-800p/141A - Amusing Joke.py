a = input()
b = input()
c = list(input())

s = list(a + b)
s.sort()
c.sort()
d = ''.join(s)
e = ''.join(c)

if d == e:
    print("YES")
else:
    print("NO")
