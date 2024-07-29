s1 = input()  
s2 = input()  

i = len(s1) - 1
j = len(s2) - 1

while i >= 0 and j >= 0:
   if s1[i] == s2[j]: 
      i -= 1
      j -= 1
   else:
      break

result = (i + 1) + (j + 1)
print(result)
