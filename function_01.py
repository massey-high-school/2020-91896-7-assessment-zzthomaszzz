import math
history_main = []

# not blank function


def not_blank(subject, error, num):
    loop = True
    while loop:
        fail = False
        response = input(subject)
        if response == "":
            print(error)
            continue
        else:
            if not num:
                for letter in response:
                    if letter.isdigit():
                        fail = True
                if fail:
                    print(error)
                    continue
                else:
                    return response
            else:
                return response


# this function get the type of shape


def get_shape(question, error):
    loop = True
    while loop:
        response = not_blank(question, error, False)
        response = response.strip()
        if response.lower() in triangle:
            response = triangle
            return response
        elif response.lower() in square:
            response = square
            return response
        elif response.lower() in rectangle:
            response = rectangle
            return response
        elif response.lower() in circle:
            response = circle
            return response
        elif response.lower() in parallelogram:
            response = parallelogram
            return response
        else:
            print(error)
            continue


# This function say the shape u chose


def say_shape(subject):
    if subject == triangle:
        print("You chose triangle")
    elif subject == square:
        print("You chose square")
    elif subject == rectangle:
        print("You chose rectangle")
    elif subject == circle:
        print("You chose circle")
    elif subject == parallelogram:
        print("You chose parallelogram")
    else:
        pass


# This function makes sure the answer only have number


def num_check(subject, error):
    loop = True
    while loop:
        fail = False
        ask = not_blank(subject, error, True)
        for letter in ask:
            if not letter.isdigit():
                fail = True
        if fail:
            print(error)
            continue
        else:
            return ask


# these functions below calculate each shape...


def calculate_tri(history):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            side_3 = num_check("Side 3: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_3)
            history_1 = ("Perimeter of a triangle: ", perimeter)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area":
            base = num_check("Base: ", "Please enter the length")
            height = num_check("Height: ", "Please enter the length")
            area = float(base) * float(height) / 2
            history_1 = ("Area of a triangle: ", area)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_square(history):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter":
            side_1 = num_check("Side: ", "Please enter the length")
            perimeter = float(side_1) * 4
            history_1 = ("Perimeter of a square: ", perimeter)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area":
            side_1 = num_check("Side: ", "Please enter the length")
            area = float(side_1) * float(side_1)
            history_1 = ("Area of a square: ", area)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_rectangle(history):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_1) + float(side_2)
            history_1 = ("Perimeter of a rectangle: ", perimeter)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            area = float(side_1) * float(side_2)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_circle():
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter":
            radius = num_check("Radius: ", "Please enter the length")
            perimeter = float(radius) * 2 * math.pi
            return perimeter
        elif question.lower() == "area":
            radius = num_check("Radius: ", "Please enter the length")
            area = float(radius) * float(radius) * math.pi
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_parallelogram():
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            side_3 = num_check("Side 3: ", "Please enter the length")
            side_4 = num_check("Side 4: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_3) + float(side_4)
            return perimeter
        elif question.lower() == "area":
            base = num_check("Base: ", "Please enter the length")
            height = num_check("Height: ", "Please enter the length")
            area = float(base) * float(height) / 2
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


# This function calculates the shape:


def calculate_main(shapes):
    if shapes == triangle:
        tri = calculate_tri(history_main)
        return tri
    if shapes == square:
        squ = calculate_square(history_main)
        return squ
    if shapes == rectangle:
        rec = calculate_rectangle(history_main)
        return rec
    if shapes == circle:
        cir = calculate_circle(history_main)
        return cir
    if shapes == parallelogram:
        para = calculate_parallelogram(history_main)
        return para


# list goes here

triangle = ["tri", "triangle", "three angle", "three angles"]
square = ["square", "sq"]
rectangle = ["rectangle", "rec"]
circle = ["circle", "no corner"]
parallelogram = ["parallelogram", " parallel"]


# testing goes here
shape = get_shape("shape: ", "Please enter a shape name")
say_shape(shape)
get_ready = calculate_main(shape)
print(get_ready)
print(history_main)
