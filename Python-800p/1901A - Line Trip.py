for _ in range(int(input())):
    n, x = map(int, input().split())
    tab = list(map(int, input().split()))
    val = 0
    max_val = 0
    for num in tab:
        max_val = max(max_val, abs(val - num))
        val = num
    print(max(max_val, abs(val - x) * 2))
