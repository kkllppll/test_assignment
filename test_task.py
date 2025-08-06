import math
import unittest

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
        data = parse_line(tokens)
        if data is None:
            continue
        perimeter, area = calculate_area_and_perimeter(data)
        print(data['type'], "perimeter:", perimeter, "area:", area)


def calculate_area_and_perimeter(data):
    if data['type'] == 'square':
        area = area_square(data['side'])
        perimeter = perimeter_square(data['side'])
    elif data['type'] == 'rectangle':
        area = area_rectangle(data['height'], data['width'])
        perimeter = perimeter_rectangle(data['height'], data['width'])
    elif data['type'] == 'circle':
        area = area_circle(data['radius'])
        perimeter = perimeter_circle(data['radius'])
    else:
        raise ValueError("Unknown shape type")
    return perimeter, area

def parse_line(tokens):
    if not tokens:
        return None
    shape_type = tokens[0].lower()
    if shape_type == 'square':
        side = float(tokens[5])
        return {'type': 'square', 'side': side}
    if shape_type == 'rectangle':
        if tokens[1].lower() == 'topright' and tokens[4].lower() == 'bottomleft':
            top = float(tokens[2])
            right = float(tokens[3])
            bottom = float(tokens[5])
            left = float(tokens[6])
            return {'type': 'rectangle', 'height': abs(bottom - top), 'width': abs(left - right)}
    if shape_type == 'circle':
        radius = float(tokens[5])
        return {'type': 'circle', 'radius': radius}
    return None

#square
def area_square(side):
    return side * side

def perimeter_square(side):
    return 4 * side

#rectangle
def area_rectangle(length, width):
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length + width)

#circle
def area_circle(r):
    return math.pi * pow(r, 2)

def perimeter_circle(r):
    return 2 * math.pi * r



class TestShapes(unittest.TestCase):
    def test_square(self):
        data = {'type': 'square', 'side': 1}
        perimeter, area = calculate_area_and_perimeter(data)
        self.assertEqual(perimeter, 4)
        self.assertEqual(area, 1)

    def test_rectangle(self):
        data = {'type': 'rectangle', 'height': 2, 'width': 4}
        perimeter, area = calculate_area_and_perimeter(data)
        self.assertEqual(perimeter, 12)
        self.assertEqual(area, 8)

    def test_circle(self):
        data = {'type': 'circle', 'radius': 2}
        perimeter, area = calculate_area_and_perimeter(data)
        self.assertAlmostEqual(perimeter, 2 * math.pi * 2)
        self.assertAlmostEqual(area, math.pi * 2 * 2)   


if __name__ == "__main__":
    main()
    #unittest.main()




