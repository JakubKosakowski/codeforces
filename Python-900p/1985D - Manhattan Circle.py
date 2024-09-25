for _ in range(int(input())):
    n, m = map(int, input().split())
    max_row = -1
    ans_row, ans_col = 0, 0
    for i in range(n):
        r = input()
        h = r.count('#')
        if h > 0:
            if max_row == -1:
                max_row = h
                ans_col = r.index('#') + 1
                ans_row = i + 1
            else:
                temp = max_row
                max_row = max(max_row, h)
                if max_row != temp:
                    ans_row = i + 1
    print(ans_row, ans_col)
