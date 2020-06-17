# Ask the user if they want to keep going...
def confirm(subject, error):
    loop = True
    while loop:
        response = input(subject)
        # neither of these answers will keep the program going
        if response.lower() == "yes" or response.lower() == "y":
            response = "yes"
            return response
        elif response.lower() == "no" or response.lower() == "n":
            response = "no"
            return response
        else:
            print(error)
            continue


ask = confirm("Do you want to keep going? ", "Please enter yes or no")