t = int(input())
for i in range(t):
    s = input()
    if len(s) % 2 == 1:
        print("NO")
    else:
        print("YES" if str(s[:len(s)//2])*2 == s else "NO")
