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
        response.strip()
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

# list goes here
triangle = ["tri", "triangle", "three angle", "three angles"]
square = ["square", "sq"]
rectangle = ["rectangle", "rec"]
circle = ["circle", "no corner"]
parallelogram = ["parallelogram", " parallel"]

# testing goes here
okay = get_shape("shape: ","Please enter a shape name")
say_shape(okay)
