# Integer checker, used for components consisting of checking integers
def number_checker(question, allow_floats=True):

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

        return response
