# checks to see if user input is an integer, if <ENTER> gives output
def guess_int_checker(question):
    while True:
        response = input(question)

        if response == "":
            print("<ENTER> IS NOT AN ACCEPTED ANSWER\n")
            continue

        error = "Please enter a valid integer\n"

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
    user_guess = guess_int_checker("Enter your guess: ")

    if user_guess in already_guessed:
        print("You've already guessed that number...\n")
        continue

    if user_guess == answer:
        print(f"Congratulations! You guessed the number on the {guesses_given} guess.\n")
        break

    else:
        guesses_given -= 1
        print(f"You've guessed incorrectly, {guesses_given} guess(es) remaining. Try Again.\n")

    already_guessed.append(user_guess)

if guesses_given == 0:
    print("You've run out of guesses. Game Over.")
