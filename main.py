
import sys
from SRC.main.menu.menu import Menu
from SRC.main.shape import Shape
from SRC.main.shapes.square import Square
from SRC.main.shapes.rectangle import Rectangle
from SRC.main.shapes.circle import Circle
from SRC.main.shapes.righttriangle import RightTriangle



if __name__ == '__main__':

    shapes = [] # זה ליסט שיחזיק  את הצורות שמזינים למערכת
    shutdown = False # כל זמן שהמשתנה הזה הוא False התוכנית מתחילה מחדש בכל פעם

    while not shutdown:
        Menu.main_menu()
        main_choice = input('Select: ')

        if main_choice == "1":
            Menu.shape_menu()
            shape = input("Select: ")

            if shape == "1":
                print("Square")
                size, color = input("set size: "), \
                              input("set color: ")
                size = float(size)
                shapes.append(Square(size, color))
            elif shape == "2":
                print("Rectangle")
                x, y, color = input("set width: "), \
                              input("set height: "),\
                              input("set color: ")
                x = float(x)
                y = float(y)
                shapes.append(Rectangle(x, y, color))
            elif shape == "3":
                print("Circle")
                radius, color = input("set radius: "), \
                                input("set color: ")
                radius = float(radius)
                shapes.append(Circle(radius, color))
            elif shape == "4":
                print("Rectangle")
                x, y, color = input("set width: "), \
                              input("set height: "), \
                              input("set color: ")
                x = float(x)
                y = float(y)
                shapes.append(RightTriangle(x, y, color))
            else:
                print("Please insert something selnsible")
                continue
        elif main_choice == "2":
            for s in shapes:
                s.details()
        elif main_choice == "3":
            circumferences = 0.0
            for s in shapes:
                circumferences += s.calc_circumference()
            print("Sum of all circumferences: {0}".format(circumferences))
        elif main_choice == "4":
            areas = 0.0
            for s in shapes:
                areas += s.calc_area()
            print("The sum of all areas: {0}".format(areas))
        elif main_choice == "5":
            results = []
            for s in shapes:
                results.append(s.calc_circumference())
            print(max(results))
        elif main_choice == "6":
            results = []
            for s in shapes:
                results.append(s.calc_area())
            print(max(results))
        elif main_choice == "7":
            print("Program exit ")
            shutdown = True
            sys.exit(0)
        else:
            print("Please concentrate and insert a proper option ")
            continue
