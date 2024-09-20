for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    print(f'{l1} {l2}' if l1 != l2 else f'{l1} {l2+1}' if l1 != l2+1 else f'{l1 + 1} {l2}')
