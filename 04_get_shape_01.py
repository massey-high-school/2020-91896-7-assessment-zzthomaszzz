# not_blank function_01
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

# ask user for the shape


def get_shape(question, error):
    loop = True
    while loop:
        response = not_blank(question, error, False)
        # removes all the spaces since the valid answers only have 1 word
        response = response.strip()
        if response.lower() in triangle:
            response = "triangle"
            return response
        elif response.lower() in square:
            response = "square"
            return response
        elif response.lower() in rectangle:
            response = "rectangle"
            return response
        elif response.lower() in circle:
            response = "circle"
            return response
        elif response.lower() in parallelogram:
            response = "parallelogram"
            return response
        else:
            print(error)
            continue

# lists for each shape


triangle = ["tri", "triangle", "three angle", "three angles", "t"]
square = ["square", "sq", "s"]
rectangle = ["rectangle", "rec", "r"]
circle = ["circle", "no corner", "c"]
parallelogram = ["parallelogram", " parallel", "p"]


ask = get_shape("Shape: ", "Please enter a shape")
print(ask)