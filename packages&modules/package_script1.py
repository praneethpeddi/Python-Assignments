try:
	import Package1
	#from Package1 import module1
	print("In Package1 module1 : import success")
	module1.a()
	module1.b()
except Exception as var:
	print(var)
	
	
'''try:
	from Package2 import module2
	print("In Package2 : import success")
	module2.c()
	module2.d()
except Exception as var:
	print(var)'''