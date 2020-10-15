def dec_to_hex_conversion(num):
	if isinstance(num, int):
		hex_value = hex(num)
		return hex_value
	else:
		print(f'This {num} cannot be converted to hexadecimal format')
	#hex_value = list(num)
	#n_hex_value = hex_value.replace("'", '')
	#for i in n_hex_value:
	#	var = ''.join(i)
	#	print(i, end='')


def main():
	"""This is a function which validates the dec_to_hex_conversion function"""
	inputs = [(1, '0x1'), (59, '0x3b'), (15,'0xf'), (19, '0x13'), ('A', '0x00'), (780, '0x30c')]
	for i in inputs:
		actual = dec_to_hex_conversion(i[0])
		if i[1] == actual:
			print(f"Validation with the number {i[0]} returned the expected value {i[1]}: Success")
		else:
			print(f"Validation with the number {i[0]} not returned the expected value {i[1]}: Failed")


if __name__ == '__main__':
	main()
