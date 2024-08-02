n = int(input())
t = input()
ans = ''
i = 1

while i < len(t)+1:
   ans += t[0]
   t = t[i:]
   i += 1

print(ans)
