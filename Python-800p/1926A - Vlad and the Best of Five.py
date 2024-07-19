d = {True: 'A', False: 'B'}

t = int(input())

for i in range(t):
    word = input()
    print(d[word.count('A') > word.count('B')])
