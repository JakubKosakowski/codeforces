s = input()
print('NO' if s.count('1') + s.count('4') != len(s) or s[0] != '1' or s.count('444') != 0 else 'YES')
