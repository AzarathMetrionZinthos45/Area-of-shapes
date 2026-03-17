class Area_Of_a_rectangle():
    def __init__(self, length, width):
        self.length = length 
        self.width = width
    def calculate(self):
        return self.length * self.width
    
length = int(input("Enter the length of the rectangle:"))
width = int(input("Enter the width of the rectangle:"))

ObjRectangle = Area_Of_a_rectangle(length, width)

print(f"the area of the rectangle is :{ObjRectangle.calculate()}")