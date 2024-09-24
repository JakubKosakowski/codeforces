n = int(input())
s = input()
print(len(s) - min(s.count('1'), s.count('0')) * 2)
