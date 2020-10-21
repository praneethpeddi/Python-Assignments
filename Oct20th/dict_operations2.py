# from CaseInsensitiveDict import *

alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'xyz': [24, 25, 26]}

def get_key_by_value(*args):
    for key, val in list(alpha.items()):
        for i in args:
            if val == i:
                print(f"{key} is key of {val}")
				
def get_value_by_case_insensitive_key(keys):
    for key, val in list(alpha.items()):
        if keys.lower() == key:
            print(f"value of the {keys}                  :   {val}")

def del_item(keys):
    for key, val in list(alpha.items()):
        if keys.lower() == key:
            del alpha[key]
            print(f"dictionary after deleting key      :   {alpha}")

def pop_element(keys):
    for key, val in list(alpha.items()):
        if keys.lower() == key:
            alpha.pop(key)
            print(f"dictionary after deleting the key   :   {alpha}")

def main():
    get_key_by_value(1, 2, 3, 4)
    get_value_by_case_insensitive_key('XyZ')
    del_item('D')
    pop_element('a')

if __name__ == "__main__":
    print(dir(dict))
    main()
