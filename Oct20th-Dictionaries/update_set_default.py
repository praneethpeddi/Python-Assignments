dict1 = {1: 'one', 2: 'two', 3: 'three'}
val1 = dict1.setdefault(4, 'four')
val2 = dict1.setdefault(5)
print(dict1)
print(val1)
print(type(val1))
print(val2)
print(type(val2))

dict3 = dict1.update({6: 'six'})
print(dict1)
print(dict3)
print(type(dict3))