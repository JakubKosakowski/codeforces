t = int(input())

for i in range(t):
   ans = 'B'
   for j in range(9):
      row = input()
      if row.count('R') == 8:
         ans = 'R'
   print(ans)
