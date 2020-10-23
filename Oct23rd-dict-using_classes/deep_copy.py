#deep copy - Deep copy is a process in which it copies the child objects found in the original. In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.

import copy
list1 = [3, 41, 561, 56]
list2 = copy.deepcopy(list1)
list2 = copy.copy(list1)
print(f"list1 = {list1}, id of list1 {id(list1)}")
print(f"list2 = {list2}, id of list2 {id(list2)}")

list1.append(56)
list2.append(45)

print(f"list1 = {list1}, id of list1 {id(list1)}")
print(f"list2 = {list2}, id of list2 {id(list2)}")