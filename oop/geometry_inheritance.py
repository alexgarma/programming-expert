import math


class Polygon:
    def get_area(self):
        raise NotImplementedError("No implementation for get_area()")

    def get_sides(self):
        raise NotImplementedError("No implementation for get_sides()")

    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_area(self):
        return get_triangle_area(self.x,self.y,self.z)
    
    def get_sides(self):
        return [self.x,self.y,self.z]
    

class Rectangle(Polygon):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_area(self):
        return get_rectangle_area(self.x,self.y)
    
    def get_sides(self):
        return [self.x,self.y] + [self.x,self.y]

class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x = x , y = x)

def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )

def get_rectangle_area(width, height):
    return width * height