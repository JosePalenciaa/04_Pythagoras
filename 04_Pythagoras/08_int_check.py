def int_checker(question):

    while True:
        response = input(question)

        error = "Please enter a valid integer (greater than 0)"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(error)
                    continue

            except ValueError:
                print(error)
                continue

        return response

# question for testing purposes...


ask_question = int_checker("How Many Fish Are There In The Ocean? ")

print("Accepted valid integer: ", ask_question)
