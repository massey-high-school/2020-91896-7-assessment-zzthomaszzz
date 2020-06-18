import math


# function goes here...


# this function check if the input is blank
def not_blank(subject, error, num):

    loop = True
    while loop:
        fail = False
        response = input(subject)
        if response == "":
            print(error)
            continue
        else:
            # if numbers are not allowed, the function will also check for number
            if not num:
                for letter in response:
                    # By going through every single letter and see if they are number or not
                    if letter.isdigit():
                        fail = True
                if fail:
                    print(error)
                    continue
                else:
                    return response
            else:
                return response


# This function get the unit from user
def get_unit(subject):
    loop = True
    while loop:
        question = input(subject)
        # removes all the blank spaces since the valid answers only have 1 word
        question = question.strip()
        if question.lower() in cm:
            question = 'cm'
            return question
        elif question.lower() in mm:
            question = 'mm'
            return question
        elif question.lower() in km:
            question = 'km'
            return question
        elif question.lower() in m:
            question = 'm'
            return question
        else:
            # error messages
            print("Please enter a unit ('cm', 'km', 'mm', 'm')")
            continue


# This function only check for "yes" and "no" questions
def confirm(subject, error):
    loop = True
    while loop:
        response = input(subject)
        # only 2 valid answers
        if response.lower() == "yes" or response.lower() == "y":
            response = "yes"
            return response
            response = "no"
        elif response.lower() == "no" or response.lower() == "n":
            return response
        else:
            # error message goes here and the loops continue
            print(error)
            continue


# This function get the shape from user
def get_shape(question, error):
    loop = True
    while loop:
        response = not_blank(question, error, False)
        # removes all the blank spaces in the answer
        response = response.strip()
        # If input is in one of the lists for shapes, the function return the shape name
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


# A simple function which just says the shape after the program gets the shape name from user
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
        # pass here because the get_shape function won't send any invalid shape
        pass


# This function check for letter in answer and makes sure there is only number in it
def num_check(subject, error):
    loop = True
    while loop:
        try:
            ask = float(input(subject))
            # The length of sides can not be zero or less since it will make it an error
            if ask <= 0:
                print(error)
            else:
                return ask

        except ValueError:
            print(error)


# This function calculates triangle dimensions
def calculate_tri(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        question = question.strip()
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            side_3 = num_check("Side 3: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_3)
            # Append this into history with  only 2 decimal places
            history_1 = ("Perimeter of a triangle: ", "{:.2f}".format(perimeter), unit)
            history.append(history_1)
            perimeter = ("{:.2f}".format(perimeter), unit)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            base = num_check("Base: ", "Please enter the length")
            height = num_check("Height: ", "Please enter the length")
            area = float(base) * float(height) / 2
            # Append this into history with  only 2 decimal places
            history_1 = ("Area of a triangle: ", "{:.2f}".format(area), unit + "2")
            history.append(history_1)
            area = ("{:.2f}".format(area), unit + "2")
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


# This function calculates square dimensions
def calculate_square(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        question = question.strip()
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side: ", "Please enter the length")
            perimeter = float(side_1) * 4
            # Append this into history with  only 2 decimal places
            history_1 = ("Perimeter of a square: ", "{:.2f}".format(perimeter), unit)
            history.append(history_1)
            perimeter = ("{:.2f}".format(perimeter), unit)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            side_1 = num_check("Side: ", "Please enter the length")
            area = float(side_1) * float(side_1)
            # Append this into history with  only 2 decimal places
            history_1 = ("Area of a square: ", "{:.2f}".format(area), unit + "2")
            history.append(history_1)
            area = ("{:.2f}".format(area), unit + "2")
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


# This function calculates rectangle dimensions
def calculate_rectangle(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        question = question.strip()
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_1) + float(side_2)
            # Append this into history with  only 2 decimal places
            history_1 = ("Perimeter of a rectangle: ", "{:.2f}".format(perimeter), unit)
            history.append(history_1)
            perimeter = ("{:.2f}".format(perimeter), unit)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            area = float(side_1) * float(side_2)
            # Append this into history with  only 2 decimal places
            history_1 = ("Area of a rectangle: ", "{:.2f}".format(area), unit + "2")
            history.append(history_1)
            area = ("{:.2f}".format(area), unit + '2')
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


# This function calculates circle dimensions
def calculate_circle(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        question = question.strip()
        if question.lower() == "perimeter" or question.lower() == "p":
            radius = num_check("Radius: ", "Please enter the length")
            perimeter = float(radius) * 2 * math.pi
            # Append this into history with  only 2 decimal places
            history_1 = ("Perimeter of a triangle: ", "{:.2f}".format(perimeter), unit)
            history.append(history_1)
            perimeter = ("{:.2f}".format(perimeter), unit)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            radius = num_check("Radius: ", "Please enter the length")
            area = float(radius) * float(radius) * math.pi
            # Append this into history with  only 2 decimal places
            history_1 = ("Area of a triangle: ", "{:.2f}".format(area), unit + "2")
            history.append(history_1)
            area = ("{:.2f}".format(area), unit + "2")
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


# This function calculates parallelogram
def calculate_parallelogram(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        question = question.strip()
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            side_3 = num_check("Side 3: ", "Please enter the length")
            side_4 = num_check("Side 4: ", "Please enter the length")
            perimeter = float(side_1) + float(side_2) + float(side_3) + float(side_4)
            # Append this into history with  only 2 decimal places
            history_1 = ("Perimeter of a parallelogram: ", "{:.2f}".format(perimeter), unit)
            history.append(history_1)
            perimeter = ("{:.2f}".format(perimeter), unit)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            base = num_check("Base: ", "Please enter the length")
            height = num_check("Height: ", "Please enter the length")
            area = float(base) * float(height) / 2
            # Append this into history with  only 2 decimal places
            history_1 = ("Area of a parallelogram: ", "{:.2f}".format(area), unit + "2")
            history.append(history_1)
            area = ("{:.2f}".format(area), unit + "2")
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


# this function follow up after get_shape to ready the dimensions formula for assigned shapes
def calculate_main(shapes):
    if shapes == triangle:
        tri = calculate_tri(history_main, unit)
        return tri
    if shapes == square:
        squ = calculate_square(history_main, unit)
        return squ
    if shapes == rectangle:
        rec = calculate_rectangle(history_main, unit)
        return rec
    if shapes == circle:
        cir = calculate_circle(history_main, unit)
        return cir
    if shapes == parallelogram:
        para = calculate_parallelogram(history_main, unit)
        return para


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
history_main = []
# Main routine goes here
loop = True
while loop:
    # Instruction...
    instruction = input("Hello, Is this your first time using this program? ")
    if instruction.lower() == "yes" or instruction.lower() == "y":
        loop_1 = True
        while loop_1:
            print("This program calculates 2 dimension for 5 shapes with 4 units")
            print("Press enter to continue")
            input("First of all, it can only calculate perimeter and area")
            input("Second, there are 5 shapes that the program able to calculate")
            print("triangle - t")
            print("square - s")
            print("rectangle - r")
            print("circle - c")
            input("parallelogram - p")
            input("Lastly, the units, there are only 4 units at the moment")
            print("Kilometer - km - k")
            print("Meter - m")
            print("Centimeter - cm - c")
            input("Millimeter - mm")
            print("To begin, the program will ask you for the shape, and then will ask you for the unit")
            input("and lastly the dimensions")
            print("After that it will give you the answer and will ask you whether you want to keep going or stop")
            print("If you choose to keep going then the program will keep going")
            print("But if you choose to stop the program will show you your history calculations")
            print("And remember, the length should be more than 0!")
            # If the user doesn't understand this instruction will loop
            okay = confirm("Do you understand this instructions? ", " Please enter either yes or no")
            if okay.lower() == "yes" or okay.lower() == "y":
                print("Okay, have fun")
                break
            else:
                print("It rewind time")
                continue
        break
    elif instruction.lower() == "no" or instruction.lower() == "n":
        print("Have fun using the calculator")
        break
    else:
        print('Please enter either yes or no')
        continue

# This loop will break when the user doesn't want to keep using the program anymore
loop_1 = True
while loop_1:
    shape = get_shape("shape: ", "Please enter a shape name")
    say_shape(shape)
    unit = get_unit("Unit: ")
    get_ready = calculate_main(shape)
    print("The answer:", get_ready[0], get_ready[1])
    go = confirm("Do you want to keep going? ", "Please say yes or no")
    if go.lower() == "yes":
        continue
    else:
        break
# This shows the user the histories of their calculatings
print("Here is your history")
print()
for i in history_main:
    print(i[0], i[1], i[2])
