try:
	import module1
	print('module1 : import success')
except Exception as var:
	print(var)
	

try:
	from module2 import c
	print("method c from module2 : import success")
except Exception as var1:
	print(var1)
	
	
