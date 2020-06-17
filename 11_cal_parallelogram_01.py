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


def calculate_parallelogram(history, unit):
    loop = True
    while loop:
        question = input("What dimension do you want to calculate? area or perimeter? ")
        if question.lower() == "perimeter" or question.lower() == "p":
            side_1 = num_check("Side 1: ", "Please enter the length")
            side_2 = num_check("Side 2: ", "Please enter the length")
            side_3 = num_check("Side 3: ", "Please enter the length")
            side_4 = num_check("Side 4: ", "Please enter the length")
            # These float() are not needed because the num_check_02 function already did this
            perimeter = float(side_1) + float(side_2) + float(side_3) + float(side_4)
            history_1 = ("Perimeter of a parallelogram: ", perimeter, unit)
            history.append(history_1)
            return perimeter
        elif question.lower() == "area" or question.lower() == "a":
            base = num_check("Base: ", "Please enter the length")
            height = num_check("Height: ", "Please enter the length")
            # These float() are not needed because the num_check_02 function already did this
            area = float(base) * float(height) / 2
            history_1 = ("Perimeter of a parallelogram: ", area, unit)
            history.append(history_1)
            return area
        else:
            print("Please enter either area or perimeter ")
            continue


history_main = []
okay = calculate_parallelogram(history_main, "cm")
for i in history_main:
    print(i)