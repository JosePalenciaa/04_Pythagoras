# Integer checker, used for components consisting of checking integers
def number_checker(question, allow_floats="yes"):

    while True:
        response = input(question)

        if response == "xxx":
            return response

        elif response != "":

            try:
                if allow_floats == "yes":
                    response = float(response)

                    if response < 1:
                        print("Please input a valid INTEGER")
                        continue

                elif allow_floats == "no":
                    response = int(response)
            except ValueError:
                print("Please input a valid NUMBER (can contain decimals)")
                continue

        return response

# Testing...


ask_integer = number_checker("Please input an integer: ", allow_floats="no")

ask_number = number_checker("Please input a number: ", allow_floats="yes")

print(f"\nInteger: {ask_integer}\t\t\tNumber: {ask_number}")
