class Calc:
    def __init__(self, x, y):
        print("In init method")
        self.x = x
        self.y = y

    def add(self):
        print(f"Addition of {self.x} and {self.y}       : {self.x + self.y}")

    def sub(self):
        print(f"Subtraction of {self.x} and {self.y}    : {self.x - self.y}")

    def mul(self):
        print(f"Multiplication of {self.x} and {self.y} : {self.x * self.y}")


obj1 = Calc(10, 60)
obj2 = Calc(30, 90)
obj1.add()
obj1.sub()
obj1.mul()
obj2.add()
obj2.sub()
obj2.mul()