n = int(input('Enter n value: '))
blank = 1
while n >= 1:
    for i in range(1, n + 1):
        print(i, end='')
    print()
    print(' '*blank, end='')
    n = n - 1
    blank = blank + 1
print()
