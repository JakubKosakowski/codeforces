t = int(input())

for i in range(t):
    words = list(map(str, input().split()))
    print(f'{words[1][0] + words[0][1:]} {words[0][0] + words[1][1:]}')
