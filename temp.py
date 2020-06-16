
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



okay = num_check("testing: ","Error")
print(okay)
