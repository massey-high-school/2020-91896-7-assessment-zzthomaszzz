# Get the unit from user
def get_unit(subject):
    loop = True
    while loop:
        question = input(subject)
        # removes any blank spaces since the unit input only has one word
        question = question.strip()
        if question in cm:
            question = "cm"
            return question
        elif question in mm:
            question = "mm"
            return question
        elif question in km:
            question = "km"
            return question
        elif question in m:
            question = "m"
            return question
        else:
            print("Please enter a unit ('cm', 'km', 'm' or 'mm')")
            continue

# these are the list for units


cm = ["cm", "c"]
km = ["km"]
mm = ["mm"]
m = ["m"]

ask = get_unit("Please tell us the unit ")
print(ask)