n = int(input())

if n % 2 == 0:
    print(n * (n // 2))
else:
    print(n * (n // 2) + (n // 2 + 1))

for i in range(n):
    if i % 2 == 0:
        print(''.join(['C'if i % 2 == 0 else '.' for i in range(n)]))
    else:
        print(''.join(['.'if i % 2 == 0 else 'C' for i in range(n)]))
