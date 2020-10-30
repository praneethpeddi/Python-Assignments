n = 3
value = 65
for i in range(n, 0, -1):
    a = 0
    for j in range(i, 0, -1):
        print(chr(value + a), end='')
        a = a + 1
    for j in range(2 * (n - i)):
        print(' ', end='')
    for j in range(i, 0, -1):
        print(chr(value + j - 1), end='')
    print("")
for i in range(1, n):
    for j in range(i + 1):
        print(chr(value + j), end='')
        a = value + j
    for j in range(2 * (n - i - 1)):
        print(' ', end='')
    for j in range(i + 1):
        print(chr(a), end='')
        a = a - 1
    print('')
