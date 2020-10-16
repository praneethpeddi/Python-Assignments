try:
	from Package2 import module2
	print('In Package2 module2 : import success')
except Exception as var:
	print(var)