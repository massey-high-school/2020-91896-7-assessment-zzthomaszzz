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


history_main = []
okay = calculate_circle(history_main, "cm")
for i in history_main:
    print(i)