from SRC.main import Shape


class Rectangle(Shape):
    # אתחול משתני הקלאס  והורשה מ Shape
    def __init__(self, x, y, color):
        super(Rectangle, self).__init__(x=x, y=y)
        self._color = color
    # חישוב והחזרת היקף מרובע
    def calc_circumference(self):
        return (self.width * 2) + (self.height * 2)
    #חישוב והחזרת שטח מרובע
    def calc_area(self):
        return self.width * self.height
    # הדפסת נתוני מרובע
    def details(self):
        print({"Form = ": Rectangle.__name__, "Width = ": self.width, "Height = ": self.height,
            "Color = ": self._color, "Area = ": self.calc_area(), "Cirecumference = ": self.calc_circumference()})
