try:
	import module2
	print("In module 2: import success")
	module2.c()
	print("function c is executed")
	module2.d()
	print("function d is executed")
except Exception as var:
	print(var)
	