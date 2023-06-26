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

# Guesses mechanics...
while guesses_given > 0:
    user_guess = int_checker("Enter your guess: ")

    if user_guess == answer:
        print(f"Congratulations! You guessed the number on the {guesses_given} guess.")

    if user_guess != answer:
        guesses_given -= 1
        print(f"You've guessed incorrectly, {guesses_given} guess(es) remaining. Try Again.")

print("You've ran out of guesses. Game Over.")
