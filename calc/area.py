shapes = ["circ", "sq", "rect", "tri"]


def calc_circ(radius):
    area = 3.14 * float(radius) * float(radius)
    return area


def calc_rect(side1, side2):
    area = float(side1) * float(side2)
    return area


def calc_tri(height, length):
    area = float(height) * float(length) / 2
    return area


def calc_sq(side):
    area = float(side) * float(side)
    return area


go_again = "yes"

while go_again == "yes":
    shape = input("Pick one - " + str(shapes) + " : ")
    if shape not in shapes:
        print("Oops that is not valid, try again.")
    elif shape == "circ":
        r = input("What is the radius of the circle? ")
        area = calc_circ(r)
        print("This is the area:", area)
    elif shape == "sq":
        s = input("What is the length of a side? ")
        area = calc_sq(s)
        print("This is the area:", area)
    elif shape == "tri":
        h = input("What is the height of the triangle? ")
        l = input("What is the length of the base? ")
        area = calc_tri(h, l)
        print("This is the area:", area)
    elif shape == "rect":
        s1 = input("What is the length of the short side? ")
        s2 = input("What is the length of the long side? ")
        area = calc_rect(s1, s2)
        print("This is the area:", area)
    go_again = input("Do you want to keep going - yes or no? ")

