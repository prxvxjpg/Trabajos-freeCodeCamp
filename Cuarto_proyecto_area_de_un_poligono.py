# Area de un polígono
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        if self.width != self.height:
            self.width = new_width
        else:
            self.width = new_width
            self.height = new_width

    def set_height(self, new_height):
        if self.width != self.height:
            self.height = new_height
        else:
            self.width = new_height
            self.height = new_height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return sum(2*val for val in vars(self).values())

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        relleno = ""
        if self.height <= 50 and self.width <= 50:
            relleno_ancho = "*" * self.width
            relleno = (relleno_ancho + "\n") * self.height
        else:
            relleno = 'Too big for picture.'
        return relleno

    def get_amount_inside(self, other):
        a = self.height // other.height
        l = self.width // other.width
        return a * l

    def __str__(self):
        string = ""
        if self.height == self.width:
            string = f"Square(side={self.height})"
        else:
            string = f"Rectangle(width={self.width}, height={self.height})"
        return string

class Square(Rectangle):
    def __init__(self, lado):
        width = lado
        height = lado
        super().__init__(width, height)

    def set_side(self, lado):
        self.height = lado
        self.width = lado

"""v1 = Rectangle(2, 3)
v1.set_height(4)
print(v1.get_area())
print(v1.get_perimeter())
print(v1.get_picture())
print(v1)"""

"""rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())"""

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())