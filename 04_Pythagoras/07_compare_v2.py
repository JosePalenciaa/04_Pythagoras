def int_checker(question):

    while True:
        response = input(question)

        error = "Please enter a valid integer"

        if response != "":
            try:
                response = float(response)

                if response < 1:
                    print(error)
                    continue

            except ValueError:
                print(error)
                continue

        return response


# question for testing purposes...
computer_answer = 10.122

while True:

    user_ans = int_checker("Guess a number: ")

    if user_ans == computer_answer:
        print("Correct Guess ✔")

    else:
        print("Wrong Guess")
