import math
class circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi *self.radius ** 2
    
r = float(input("Enter the radius:"))

cj = circle(r)
print(f"Area of the circle is: {cj.area()}")