# assigning using assignment operator

dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
dict2 = dict1
dict2.clear()
print(dict1)
print(type(dict1))
print(dict2)
print(type(dict2))
print()

# assigning using the copy method

dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
dict2 = dict1.copy()
dict2.clear()
print(dict1)
print(type(dict1))
print(dict2)
print(type(dict2))