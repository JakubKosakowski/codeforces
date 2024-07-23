t = int(input())

for i in range(t):
   num = int(input())
   ans = num // 10 + 1 if str(num)[-1] == '9' else num // 10
   print(ans)
