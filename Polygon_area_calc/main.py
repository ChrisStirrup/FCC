class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width
        return

    def set_height(self, height):
        self.height = height
        return

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        perimeter = (2 * (self.width + self.height))
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_amount_inside(self, shape_to_fit):
        amount_inside = ((self.height // shape_to_fit.height) * (self.width // shape_to_fit.width))
        return amount_inside

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            first_row = ''
            picture = ''
            make_first_row = self.width
            while make_first_row > 1:
                first_row += '*'
                make_first_row -= 1
            first_row += '* \n'
            make_columns = self.height
            while make_columns > 0:
                picture += first_row
                make_columns -= 1
            return picture


class Square(Rectangle):
    def __init__(self, side):
        self.side = self.width = self.height = side

    def __str__(self):
        return "Square(side={})".format(self.side)

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side
        return


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))