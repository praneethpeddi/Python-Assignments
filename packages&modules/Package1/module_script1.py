try:
	import module1
	print('In module1 : import success')
	module1.a()
	print("Function a executed")
	module1.b()
	print("Function b executed")
except Exception as var:
	print(var)
	
try:
	