# Check if the answer is blank or contain number (if numbers aren't allowed)
def not_blank(subject, error, num):
    loop = True
    while loop:
        fail = False
        response = input(subject)
        if response == "":
            print(error)
            continue
        else:
            # if numbers are not allowed, this will check for number in the string
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


test = not_blank("Testing (number allowed): ", "Please enter something doesn't contain numbers", False)
