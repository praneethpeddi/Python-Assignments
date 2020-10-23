class Dict:
    alpha = {}

    def __init__(self, data):
        print(f"In init method")
        self.data = data
        print(f"original dictionary           :   {self.data}")
        for key, value in data.items():
            self.alpha[key] = value
            self.alpha[value] = key

    def __getitem__(self, key):
        try:
            if isinstance(key, int):
                res = self.alpha[key]
                return res
            else:
                res = self.alpha[key.lower()]
                return res
        except KeyError as var:
            print(f"{var} key not found ")

    def __delitem__(self, key):
        try:
            del self.data[key.lower()]
            print(f"after deleting the key {key}    :   {self.data}")
        except KeyError as var:
            print(f"{var} key not found ")

    def __setitem__(self, key, value):
        self.data[key.lower()] = value
        print(f"after adding the key {key}        :   {self.data}")

    def __len__(self):
        print(f"length of the dictionary      :   {len(self.data)}")

    def __index__(self, key):
        print(f"Index number of the key, {key}    :   {self.data[key]}")

    def get_values(self):
        return self.data.values()

    def get_keys(self):
        return self.data.keys()

    def get_items(self):
        return self.data.items()


obj1 = Dict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'xyz': 3890})
print(f"Value for the key             :   {obj1['A']}")
print(f"Value for the key XYZ         :   {obj1['XYZ']}")
print(f"Key for the value             :   {obj1[3890]}")
obj1.__delitem__('xyz')
obj1['e'] = 5
obj1['name'] = 'Praneeth'
obj1.__len__()
obj1.__index__('a')
print(f"Items of the dictionary       :   {obj1.get_items()}")
print(f"values of the dictionary`     :   {obj1.get_values()}")
print(f"keys of the dictionary        :   {obj1.get_keys()}")