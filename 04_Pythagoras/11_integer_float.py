# Integer checker, used for components consisting of checking integers
def number_checker(question, allow_floats="yes"):

    while True:
        response = input(question)

        error = "Please enter a valid integer\n"

        if response == "xxx":
            return response

        elif response != "":
            try:
                response = int(response)

                if response < 1:
                    print(error)
                    continue

            except ValueError:
                print(error)
                continue

        try:
            if allow_floats == "yes":
                response = float(response)

            elif allow_floats == "no":
                response = int(response)
        except ValueError:
            print("Please enter a valid number")
            continue

        return response

# Testing...


user_integer = number_checker("Please input an integer: ", allow_floats="no")

user_number = number_checker("Please input a number: ", allow_floats="yes")

print(f"\nInteger: {user_integer}\t\t\tNumber: {user_number}")
