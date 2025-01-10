from take_user_data import TakeUserInput


# Simple Python program to calculate the area of a rectangle

class Rectangle:
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width
    
    def calculate_area(self):
        return self.length * self.width
    

if __name__ == '__main__':
    length = float(TakeUserInput.take_user_input_rectangle_length())
    width = float(TakeUserInput.take_user_input_rectangle_width())

    rectangle = Rectangle(length, width)

    result = rectangle.calculate_area()

    print(f"result : {result}")


