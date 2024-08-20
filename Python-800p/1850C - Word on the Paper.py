t = int(input())

for i in range(t):
    text = ''
    for j in range(8):
        line = input()
        text += line.replace('.', '')
    print(text)
