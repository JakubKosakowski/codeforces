t = int(input())

for i in range(t):
	d = {}
	ans = 0
	let = input()
	s = input()
	for i, c in enumerate(let):
		d[c] = i + 1
	pos = d[s[0]]
	for i in range(1, len(s)):
		ans += abs(pos - d[s[i]])
		pos = d[s[i]]
	print(ans)
