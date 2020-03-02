# Base Class
class Shape:
    # מידות לקליטה - כולן מוגדרות כ- float
    width = 0.0
    height = 0.0
    radius = 0.0
    # אתחול משתני הקלאס
    def __init__(self, x=None, y=None, r=None):
        #הכוונה הראשונית היא להגדיר את המשתנים כ- float אבל אני רוצה לתת להם את הערך None בזמן האתחול
        self.width = x
        self.height = y
        self.radius = r
    # קבלת משתנה והחזרתו
    def get(self, field):
        if field == 'width':
            return self.width
        elif field == 'height':
            return self.height
        elif field == 'radius':
            return self.radius
        else:
            raise AttributeError('Nothing doing "{0}"'.format(__name__))
    # קביעת ערך למשתנים
    def set(self, field, value):
        if field == 'width':
            self.width = value
        elif field == 'height':
            self.height = value
        elif field == 'radius':
            self.radius = value
        else:
            raise AttributeError('No such attribute associated to "{0}"'.format(__name__))

    def calc_area(self):
        ...


    def calc_circumference(self):
        ...

