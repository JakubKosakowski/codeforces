t = input()

if int(t) >= 0:
   print(int(t))
else:
   print(max([int(t[:-1]), int(t[:-2] + t[-1])]))
