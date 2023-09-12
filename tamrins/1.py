class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x: {self.x}\ny: {self.y}"
p1 = Point(200, 100)
p2 = Point(100, 300)
p3 = Point(0, -100)
p4 = Point()
print('-'*20)
print(p1)
print('-'*20)
print(p2)
print('-'*20)
print(p3)
print('-'*20)
print(p4)
print('-'*20)
