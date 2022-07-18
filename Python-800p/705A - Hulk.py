n = int(input())
temp = 0
d = ""

while True:
    if temp % 2 == 0:
        d += "I hate"
        temp += 1
    else:
        d += "I love"
        temp += 1
    if temp == n:
        break
    d += " that "

d += " it"
print(d)
