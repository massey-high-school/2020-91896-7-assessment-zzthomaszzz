# a better and simpler version of num_check
def num_check(subject, error):
    loop = True
    while loop:
        try:
            # if input not float then the program will loop and complain
            ask = float(input(subject))
            # This function will be used for getting length for sides so the answer should be more than 0
            if ask <= 0:
                print(error)
            else:
                return ask
        except ValueError:
            print(error)


hi = num_check("Number: ", "Error")
print(hi)