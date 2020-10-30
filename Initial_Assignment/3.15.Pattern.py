n = int(input('Enter a number: '))
value = 0
for i in range(0, n + 1):
    for j in range(0, 2 * n - 1):
        if j >= n:
            value = value - 1
        else:
            value = value + 1
        if value > i:
            print(' ', end=' ')
        else:
            print(value, end=' ')
    value = 0
    print()