t = int(input())

for i in range(t):
	tab = list(map(int, input().split()))
	tab.sort()
	print(abs(tab[1] - tab[0]) + abs(tab[1] - tab[2]))
