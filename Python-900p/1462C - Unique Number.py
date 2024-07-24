t = int(input())

for i in range(t):
   n = int(input())
   if n < 10:
      print(n)
   elif n > 45:
      print(-1)
   else:
      ans = 0
      start_num = 9
      j = 0
      while True:
         ans += start_num * 10 ** j
         j += 1
         if n - start_num <= start_num - 1:
            ans += (n - start_num) * 10 ** j
            break
         else:
            n -= start_num
            start_num -= 1
      print(ans)
