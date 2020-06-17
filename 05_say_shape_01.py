# Say the shape after user input their answer for get_shape_01
def say_shape(subject):
    loop = True
    while loop:
        # this input wont have in the assembled program because get_shape_01 will be doing this
        ask = input(subject)
        if ask == "triangle":
            print("You chose triangle")
            return ask
        elif ask == "square":
            print("You chose square")
            return ask
        elif ask == "rectangle":
            print("You chose rectangle")
            return ask
        elif ask == "circle":
            print("You chose circle")
            return ask
        elif ask == "parallelogram":
            print("You chose parallelogram")
            return ask
        else:
            print("Please enter a shape")
            continue


okay = say_shape("Shape: ")
