try:
	from package1 import module1
	print('module1 : import success')
except Exception as var:
	print(var)
	
try:
	from package1 import module2
	print("module2 : import success")
except Exception as var1:
	print(var1)