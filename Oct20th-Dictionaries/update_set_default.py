dict1 = {1: 'one', 2: 'two', 3: 'three'}
print(dict1)
val1 = dict1.setdefault(4, 'four')
val2 = dict1.setdefault(5)
print(dict1.setdefault(4))
print(dict1)
print(val1)
print(val2)
print(type(val1))
print(type(val2))

val3 = dict1.update({6: 'six'})
val4 = dict1.update({7: ''})
print(dict1)
print(val3)
print(val4)
print(type(val3))
print(type(val4))
