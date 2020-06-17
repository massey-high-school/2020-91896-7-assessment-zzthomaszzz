# not_blank_01
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

# num_check_01 with lots of errors


def num_check_1(subject, error):
    loop = True
    while loop:
        fail = False
        # This input will only accept float but not string
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
            # if input can't be converted then it will be an error
            ask = str(ask)
            return ask


okay = num_check_1("Enter a number", "error")
print(okay)