dict1 = {'1':'one', '2':'two', '3':'three', '4':'four'}

print(f"Original dictionary                                         :   {dict1}")
print(f"all the keys from the dictionary                            :   {list(dict1.keys())}")
print(f"all the values from the dictionary                          :   {dict1.values()}")
print(f"all the items in the dictionary                             :   {dict1.items()}")
dict1['5'] = 'five'
print(f"updated dictionary                                          :   {dict1}")
del dict1['5']
print(f"dictionary after deleting the key 5                         :   {dict1}")
dict2 = dict1.copy()
print(f"copying dict1 key,value pairs to dict2                      :   {dict2}")
dict2.clear()
print(f"deleting all the copied elements from dict2:                :   {dict2}")
dict1.pop('1')
print(f"dictionary after deleting the key 1                         :   {dict1}")
dict1.popitem()
print(f"dictionary after deleting last key,value pair               :   {dict1}")
dict1.update({'1':'one'})
print(f"dictionary after updating the key,value pair                :   {dict1}")

dict_of_stu = {'stu_data': ['Praneeth', [45, 67, 78, 89, 99]]}

print(f"name of the student                                         :   {dict_of_stu['stu_data'][0]}")
print(f"marks of the student {dict_of_stu['stu_data'][0]}           :   {dict_of_stu['stu_data'][1]}")
print(f"highest marks of the student {dict_of_stu['stu_data'][0]}   :   {max(dict_of_stu['stu_data'][1])}")

dict_of_emp = {'name':'xyz', 'age':46, 'position':'Engineer', 'mailid':['xyz@gmail.com', 'abc@gmail.com']}

print(f"employee data in dict format                                :   {dict_of_emp}")
print(f"name of the employee                                        :   {dict_of_emp['name']}")
print(f"age of the employee                                         :   {dict_of_emp['age']}")
print(f"postion of the employee                                     :   {dict_of_emp['position']}")
print(f"emails of the emplyee                                       :   {dict_of_emp['mailid']}")
dict_of_emp['name'] = 'abc'
print(f"employee data in dict format after updating the name        :   {dict_of_emp}")

keys = dict_of_emp.get('gender')

if keys in dict_of_emp:
    print(keys)
else:
    print("key not present")

for ele in list(dict_of_emp.items()):
    print(ele)


