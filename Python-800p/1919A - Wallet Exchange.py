d = {True: 'Bob', False: 'Alice'}

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(d[(a + b) % 2 == 0])
