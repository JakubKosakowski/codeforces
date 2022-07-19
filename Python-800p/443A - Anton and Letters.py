s = list(input())

check = [i for i in s if ord(i) >= 97 and ord(i) <= 122]

result = ''.join(check)

print(len(set(result)))
