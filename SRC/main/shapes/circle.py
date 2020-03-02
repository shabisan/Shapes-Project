from math import pi
from SRC.main import Shape


class Circle(Shape):
    # אתחול משתני הקלאס  והורשה מ Shape
    def __init__(self, radius, color):
        super(Circle, self).__init__(r=radius)
        self._color = color
    # חישוב והחזרת היקף עגול
    def calc_circumference(self):
        return (self.radius * pi) * 2
    # חישוב והחזרת שטח עיגול
    def calc_area(self):
        return pi * (self.radius * self.radius)
    # הדפסת הנתונים של העיגול
    def details(self):
        print({ "Form = ": Circle.__name__, "Width = ": self.width, "Height = ": self.height,
            "Color = ": self._color, "Area = ": self.calc_area(), "Circumference = ": self.calc_circumference()})
