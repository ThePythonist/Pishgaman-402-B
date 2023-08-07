from math import pi


class Shape:
    def __init__(self, l=0, w=0, r=0, ):
        self.radius = r
        self.length = l
        self.width = w

    def perimeter1(self):
        print(2 * self.radius * 3.14)

    def perimeter2(self):
        print((self.length + self.width) * 2)

    def area1(self):
        print(self.radius * self.radius * pi)

    def area2(self):
        print(self.length * self.width)


# Instance ( Shey )

shape = input("""
1 : Circle
2 : Rectangle
Choose :
""")

if shape == "1":
    r = int(input("Enter radius : "))
    circle = Shape(r=r)
    print("Circle Perimeter : ", end="")
    circle.perimeter1()
    print("Circle Area : ", end="")
    circle.area1()
elif shape == "2":
    l = int(input("Enter length : "))
    w = int(input("Enter width : "))
    rectangle = Shape(l=l, w=w)
    print("Rectangle Perimeter : ", end="")
    rectangle.perimeter2()
    print("Rectangle Area : ", end="")
    rectangle.area2()
