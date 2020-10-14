num = 7
hex_value = list(hex(num))
hex_value.insert(2, '0')
for i in hex_value:
    print(''.join(i), end='')