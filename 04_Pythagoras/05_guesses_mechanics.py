# checks to see if user input is an integer
def int_checker(question):

    while True:
        response = input(question)

        error = "Please enter a valid integer"

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


guesses_given = 3


# Answer set for testing purposes...
answer = 3

while guesses_given > 0:
    user_guess = int_checker("Enter your guess: ")

    if user_guess == answer:
        print("Congratulations! You guessed correctly.")

    elif user_guess != answer:
        print("You've guessed incorrectly.")

    guesses_given -= 1

print("You've ran out of guesses. Game Over.")
