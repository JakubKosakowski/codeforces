d = {True: 'Yes', False: 'No'}

n = int(input())

for i in range(n):
   n, m = list(map(int, input().split()))
   print(d[n == m or (n > m and n % 2 == m % 2)])
