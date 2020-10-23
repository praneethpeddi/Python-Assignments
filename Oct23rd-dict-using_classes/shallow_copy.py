# shallow copy - The copying process does not create copies of the child objects themselves and only a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.

import copy

list1 = [3, 41, 561, 56]
list2 = list1
print(f"list1 = {list1}, id of list1 {id(list1)}")
print(f"list2 = {list2}, id of list2 {id(list2)}")

list2.append(45)

print(f"list1 = {list1}, id of list1 {id(list1)}")
print(f"list2 = {list2}, id of list2 {id(list2)}")

