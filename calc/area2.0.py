import numbers

shapes = ["C", "T", "R"]


def Circle(r):
    a = r * r * 3.14
    return a


def Triangle(h, l):
    a = h * l / 2
    return a


def Rectangle(s, l):
    a = s * l
    return a


def convertToNumber(str):
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            return str


calc_or_not = True

while calc_or_not:
    what_calc = str(input("What shape would you like to calculate: C, T or R: "))
    what_calc = what_calc.upper()
    if what_calc not in shapes:
        print("Sorry, that's not a valid command.")
    elif what_calc == "C":
        radius = input("What is the radius of the circle: ")
        radius = convertToNumber(radius)
        if isinstance(radius, numbers.Number):
            radius = int(radius)
            a = Circle(radius)
            print("The area of that circle is ", a)
        else:
            print("Input is NOT a number, please try again")
    elif what_calc == "T":
        height = input("What is the height of the triangle")
        length = input("What is the length of the triangle")
        height = convertToNumber(height)
        length = convertToNumber(length)
        if isinstance(height, numbers.Number) and isinstance(length, numbers.Number):
            height = int(height)
            length = int(length)
            a = Triangle(height, length)
            print("The area of that triangle is ", a)
    elif what_calc == "R":
        l_side = input("What is the length of the long side")
        s_side = input("What is the length of the short side")
        l_side = convertToNumber(l_side)
        s_side = convertToNumber(s_side)
        if isinstance(l_side, numbers.Number) and isinstance(s_side, numbers.Number):
            l_side = int(l_side)
            s_side = int(s_side)
            a = Rectangle(s_side, l_side)
            print("The area of that rectangle is ", a)

