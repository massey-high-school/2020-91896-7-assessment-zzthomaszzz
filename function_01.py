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


def get_unit(subject):
    loop = True
    while loop:
        question = input(subject)
        question = question.strip()
        if question in cm:
            question = cm
            return question
        elif question in mm:
            question = mm
            return question
        elif question in km:
            question = km
            return question
        elif question in m:
            question = m
            return question
        else:
            print("Please enter a unit ('cm', 'km', 'mm)")
            continue


def confirm(subject, error):
    loop = True
    while loop:
        response = input(subject)
        if response == "":
            print(error)
            continue
        elif response.lower() == "yes" or response.lower() == "y":
            response = "yes"
            return response
        elif response.lower() == "no" or response.lower() == "n":
            response = "no"
            return response
        else:
            print(error)
            continue


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


def num_check_1(subject, error):
    loop = True
    while loop:
        fail = False
        ask = float(not_blank(subject, error, True))
        if ask <= 0 or ask == "0":
            print("The length must be more than 0")
            continue
        for letter in ask:
            if letter.isalpha():
                fail = True
        if fail:
            print(error)
            continue
        else:
            ask = str(ask)
            return ask


def num_check(subject, error):
    loop = True
    while loop:
        try:
            ask = float(input(subject))
            if ask <= 0:
                print(error)
            else:
                return ask

        except ValueError:
            print(error)


def calculate_tri(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            side_3 = num_check("Side 3: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_3)
            history_1 = ("Perimeter of a triangle: ", perimeter, unit)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            base = num_check("Base: ", "Please enter the length")
            height = num_check("Height: ", "Please enter the length")
            area = float(base) * float(height) / 2
            history_1 = ("Area of a triangle: ", area, unit)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_square(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side: ", "Please enter the length")
            perimeter = float(side_1) * 4
            history_1 = ("Perimeter of a square: ", perimeter, unit)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            side_1 = num_check("Side: ", "Please enter the length")
            area = float(side_1) * float(side_1)
            history_1 = ("Area of a square: ", area, unit)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_rectangle(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_1) + float(side_2)
            history_1 = ("Perimeter of a rectangle: ", perimeter, unit)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            area = float(side_1) * float(side_2)
            history_1 = ("Area of a rectangle: ", area, unit)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_circle(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter" or question.lower() == "p":
            radius = num_check("Radius: ", "Please enter the length")
            perimeter = float(radius) * 2 * math.pi
            history_1 = ("Perimeter of a triangle: ", perimeter, unit)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            radius = num_check("Radius: ", "Please enter the length")
            area = float(radius) * float(radius) * math.pi
            history_1 = ("Area of a triangle: ", area, unit)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_parallelogram(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            side_3 = num_check("Side 3: ", "Please enter the length")
            side_4 = num_check("Side 4: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_3) + float(side_4)
            history_1 = ("Perimeter of a parallelogram: ", perimeter, unit)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            base = num_check("Base: ", "Please enter the length")
            height = num_check("Height: ", "Please enter the length")
            area = float(base) * float(height) / 2
            history_1 = ("Perimeter of a parallelogram: ", area, unit)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


def calculate_main(shapes):
    if shapes == triangle:
        unit = get_unit("Please enter a unit")
        tri = calculate_tri(history_main, unit)
        return tri
    if shapes == square:
        unit = get_unit("Please enter a unit")
        squ = calculate_square(history_main, unit)
        return squ
    if shapes == rectangle:
        unit = get_unit("Please enter a unit")
        rec = calculate_rectangle(history_main, unit)
        return rec
    if shapes == circle:
        unit = get_unit("Please enter a unit")
        cir = calculate_circle(history_main, unit)
        return cir
    if shapes == parallelogram:
        unit = get_unit("Please enter a unit")
        para = calculate_parallelogram(history_main, unit)
        return para












# This function calculates the shape:


# list goes here

triangle = ["tri", "triangle", "three angle", "three angles", "t"]
square = ["square", "sq", "s"]
rectangle = ["rectangle", "rec", "r"]
circle = ["circle", "no corner", "c"]
parallelogram = ["parallelogram", " parallel", "p"]
cm = ["cm"]
km = ["km"]
mm = ["mm"]
m = ["m"]
# testing goes here
loop_1 = True
while loop_1:
    shape = get_shape("shape: ", "Please enter a shape name")
    say_shape(shape)
    get_ready = calculate_main(shape)
    print("The answer: ", get_ready)
    go = confirm("Do you want to keep going? ", "Please say yes or no")
    if go.lower() == "yes":
        continue
    else:
        break

for i in history_main:
    print(i)
