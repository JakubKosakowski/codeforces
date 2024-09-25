a = int(input())
b = int(input())
c = a + b
print('YES' if int(str(a).replace('0', '')) + int(str(b).replace('0', '')) == int(str(c).replace('0', '')) else 'NO')
