n = int(input('Enter n value: '))
value = 0
temp = n
while n > 0:
    for i in range(0, 2 * temp - 1):
        if i >= temp:
            value = value - 1
        else:
            value = value + 1
        if value <= n:
            print(value, end=' ')
        else:
            print(' '*2, end='')
    value = 0
    n = n - 1
    print()