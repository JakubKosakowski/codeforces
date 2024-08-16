
d = {}
j = 1
for i in range(97, 123):
    d[chr(i)] = j
    j += 1

s = input()
cur_pos = 'a'
ans = 0
for c in s:
    ans += min([abs(d[c] - d[cur_pos]), d[cur_pos] + (26 - d[c]), (26 - d[cur_pos]) + d[c]])
    cur_pos = c
print(ans)
