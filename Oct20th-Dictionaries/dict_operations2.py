# from CaseInsensitiveDict import *

def get_key_by_value(*args):
    for key, val in list(alpha.items()):
        for i in args:
            if val == i:
                print(f"{key} is key to value {val}")


def get_value_by_case_insensitive_key(keys):
    for key, val in list(alpha.items()):
        if keys.lower() == key:
            print(f"value of the {keys}                                 :   {val}")


def del_item(keys):
    for key, val in list(alpha.items()):
        if keys.lower() == key:
            del alpha[key]
            print(f"dictionary after deleting key using del method   :   {alpha}")


def pop_element(keys):
    for key, val in list(alpha.items()):
        if keys.lower() == key:
            alpha.pop(key)
            print(f"dictionary after deleting key using pop method   :   {alpha}")


def main():
    get_key_by_value(1, 2, 3, 4, [24, 25, 26])
    get_value_by_case_insensitive_key('XYZ')
    del_item('D')
    pop_element('A')


if __name__ == "__main__":
    alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'xyz': [24, 25, 26]}
    print(f"Original Dictionary                              :   {alpha}")
    main()