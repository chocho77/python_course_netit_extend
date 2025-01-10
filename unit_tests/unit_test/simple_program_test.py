import unittest
from simple_program import Rectangle


# The function to calculate the area
#def calculate_area(length, width):
#    return length * width

class TestRectangleAreaCalculator(unittest.TestCase):

    rectangle = Rectangle(9.0, 2.0)
    
    def test_area(self):
        rectangle = Rectangle(9.0, 2.0)
        self.assertEqual(rectangle.calculate_area(), 18.0)
        rectangle = Rectangle(2.0, 2.0)
        self.assertEqual(rectangle.calculate_area(), 4.0)
        


if __name__ == "__main__":
    unittest.main()
