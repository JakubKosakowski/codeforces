s = input()
temp = s.count('a')
temp2 = len(s) - temp
print(len(s) if temp > len(s) // 2 else len(s) - (temp2 - temp + 1))
