class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление" + str(self))


pt = Point(1, 2)
# print(pt.__dict__)
# print(Point.__dict__)
a = pt
# b = pt
a.__del__()
del a
# print(pt.__dict__)
print(a.__dict__)
# print(b.__dict__)


