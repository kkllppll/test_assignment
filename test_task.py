import math
import unittest


class Shape():
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError
    

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side



    
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius    
    
    def area(self):
        return math.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    


def main():
    print("Enter the shape data. Example 'Square TopRight 1 1 Side 1'. Print 'stop' to end input:")
    input_lines = []
    while True:
        try:
            
            line = input()
            if line.strip().lower() == "stop":
                print("Input ended.")
                break
            if line.strip() == "":
                continue
            input_lines.append(line)
        except:
            break

    for line in input_lines:
        tokens = line.strip().split()
        shape = parse_line(tokens)
        if shape is None:
            continue
        print(type(shape).__name__, "perimeter:", shape.perimeter(), "area:", shape.area())                 




def parse_line(tokens):
    if not tokens:
        return None
    shape_type = tokens[0].lower()

    if shape_type == 'square':
        side = float(tokens[5])
        return Square(side)
    
    if shape_type == 'rectangle':
        if tokens[1].lower() == 'topright' and tokens[4].lower() == 'bottomleft':
            top = float(tokens[2])
            right = float(tokens[3])
            bottom = float(tokens[5])
            left = float(tokens[6])
            return Rectangle(abs(top - bottom), abs(right - left))
        
    if shape_type == 'circle':
        radius = float(tokens[5])
        return Circle(radius)
    
    return None





class TestShapes(unittest.TestCase):
    def test_square(self):
        square = Square(1)
        self.assertEqual(square.perimeter(), 4)
        self.assertEqual(square.area(), 1)

    def test_rectangle(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.perimeter(), 12)
        self.assertEqual(rectangle.area(), 8)

    def test_circle(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * 2)
        self.assertAlmostEqual(circle.area(), math.pi * 2 * 2)   


if __name__ == "__main__":
    #main()
    unittest.main()




