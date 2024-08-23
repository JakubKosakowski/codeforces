d = {True: 'First', False: 'Second'}

t = int(input())

for i in range(t):
	a, b, c = list(map(int, input().split()))
	print(d[a + (c // 2 + c % 2) > b + (c // 2)])
