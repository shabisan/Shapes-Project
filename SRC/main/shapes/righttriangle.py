from SRC.main import Shape
from math import sqrt

class RightTriangle(Shape):
    # אתחול משתני הקלאס  והורשה מ Shape
    def __init__(self, x, y, color):
        super(RightTriangle, self).__init__(x=x, y=y)
        self._color = color
    # חישוב והחזרת היקף משולש
    def calc_circumference(self):
        return (self.width * self.height) / 2
    # חישוב והחזרת שטח משולש
    def calc_area(self):
        a = self.width + self.height
        b = self.width * self.width
        c = self.height * self.height
        return a + sqrt(b+c)
    # הדפסת נתוני משולש
    def details(self):
        print({"Form = ": RightTriangle.__name__, "Width = ": self.width, "Height = ": self.height,
            "Color = ": self._color, "Area = ": self.calc_area(), "Circumference = ": self.calc_circumference()})
