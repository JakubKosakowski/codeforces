def has_even_digit(num):
    while num != 0:
        result = 0
        i = 1
        digit = num % 10
        if digit % 2 == 0:
            return True
        else:
            result += digit * i
            i *= 10
            num = num // 10
    return False

for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0 :
        print(0)
        continue
    if str(n)[0] in ['2', '4', '6', '8']:
        print(1)
        continue
    elif has_even_digit(n):
        print(2)
        continue
    else:
        print(-1)
        continue
