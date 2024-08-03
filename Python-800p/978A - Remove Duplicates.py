t = int(input())

tab = list(map(int, input().split()))
ans = {}
for num in tab[::-1]:
   if num not in ans:
      ans[num] = 1
ans = [str(x) for x in ans.keys()]

print(len(ans))
print(" ".join(ans[::-1]))
