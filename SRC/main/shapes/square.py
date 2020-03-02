from SRC.main import Shape


class Square(Shape):
    # אתחול משתני הקלאס  והורשה מ Shape
    def __init__(self, size, color):
        super(Square, self).__init__(x=size, y=size)
        self._color = color
    #חישוב והחזרת היקף ריבוע
    def calc_circumference(self):
        return self.width * 4
    # חישוב והחזרת שטח ריבוע
    def calc_area(self):
        return self.width * self.width
    # הדפסת נתוני ריבוע
    def details(self):
        print({"Form = ": Square.__name__, "Width = ": self.width, "Height = ": self.height,
            "Color = ": self._color, "Area = ": self.calc_area(), "Cirdumference = ": self.calc_circumference()})
