d = {True: 'YES', False: 'NO'}

t = int(input())

for i in range(t):
   n = int(input())
   s = input()
   flag = True
   test = 'Timur'
   if n != 5:
      print('NO')
      continue
   for c in s:
      if c in test:
         test = test.replace(c, '')
      else:
         flag = False
         break
   print(d[flag])
