s = input()
ans = ''
for c in s:
    if c.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        continue
    ans += f'.{c.lower()}'
print(ans)
