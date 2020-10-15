inputs = [(1, 0x1), (59, 0x3b)]
for i in inputs:
	hex_val = hex(i[0])
	print(hex_val)
	print(type(hex_val))
	n_val = list(hex_val)
	for i in n_val:
		print(i, end='')
	print()
	
print(inputs[0])
print(inputs[1])
