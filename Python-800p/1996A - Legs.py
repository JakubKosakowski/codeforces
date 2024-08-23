t = int(input())

for i in range(t):
	legs = int(input())
	cows = legs // 4
	legs -= cows * 4
	chickens = legs // 2
	print(cows + chickens)
