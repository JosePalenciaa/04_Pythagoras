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


# Guess(es) value and already guessed list...
guesses_given = 3
already_guessed = []

# Answer set for testing purposes...
answer = 3

# Guesses mechanics...
while guesses_given > 0:
    user_guess = int_checker("Enter your guess: ")

    if user_guess in already_guessed:
        print("You've already guessed that number...")
        continue

    if user_guess == answer:
        print(f"Congratulations! You guessed the number on the {guesses_given} guess.")

    elif user_guess != answer:
        guesses_given -= 1
        print(f"You've guessed incorrectly, {guesses_given} guess(es) remaining. Try Again.")

    already_guessed.append(user_guess)

print("You've ran out of guesses. Game Over.")
