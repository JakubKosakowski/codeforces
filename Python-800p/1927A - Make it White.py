t = int(input())

for i in range(t):
    n = int(input())
    row = input()
    first = row.index('B')
    last = row[::-1].index('B')
    print(len(row[first:len(row)-last]))
