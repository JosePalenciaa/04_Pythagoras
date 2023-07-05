import math
import random


# Functions go here...

# Displays instructions function
def instructions():
    print("---------------------")
    print("**** How to Play ****")
    print("---------------------")
    print()
    print("Your goal is to calculate the missing side using the 'Pythagorean Theorem'..."
          "\n• Formulas:\n\tHypotenuse | a² + b² = c²\n\tOpposite | c² - a² = b²\n\tAdjacent | c² - b² = a²"
          "\n\tHypotenuse = c | Opposite / Adjacent = b / a"
          "\n\n• First select a difficulty."
          "\n• You are given 3 attempts. "
          "\n• Solve the missing side. "
          "\n• Round your answer to the nearest decimal place."
          "\n• Can you win?")


# Yes / no / why response function
def yes_no_why(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no / why)")
        print()


# Integer checker, used for components consisting of checking integers
def int_checker(question):

    while True:
        response = input(question)

        error = "Please enter a valid integer greater than 0"

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


# Function that lets the user choose the difficulty
def difficult(question):
    while True:
        response = input(question).lower()

        for item in diff_list:
            if response == item[0] or response == item:
                return item

        print("!!! Please choose a valid difficulty !!!")
        print()


# Checks to see if user input is a valid number, if <ENTER> gives output
def guess_float_checker(question):
    while True:
        response = input(question)

        if response == "xxx":
            return response

        if response == "":
            print("<ENTER> IS NOT AN ACCEPTED ANSWER\n")
            continue

        error = "Please enter a valid number (only 1 d.p)\n"

        try:
            response = float(response)

            if response < 1:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        return response


# Lists go here...

# list of accepted values for yes / no checker
yesno_list = ["yes", "no", "why"]

# list for accepted values of difficulty
diff_list = ["easy", "medium", "hard"]

difficulty = ""

# Main Routine goes here...

# Introduction / title of game
print("######################################")
print("!!! Welcome to the Pythagoras Quiz !!!")
print("######################################")
print()

# Looping so user response of 'why' gives the response, and asks the question again
while True:
    # Asks user for a response (related to the instructions)
    display_instructions = yes_no_why("Do you want to see the INSTRUCTIONS? ")

    # Gets angry at user if they respond with 'why', loop continues
    if display_instructions == "why":
        print("Because I said so!!!")
        print()
        continue

    # Displays instructions of user says 'yes', loop breaks and continues with rest of code
    elif display_instructions == "yes":
        print()
        instructions()
        break

    # Outputs a statement if user says 'no', loop breaks and continues with rest of code
    elif display_instructions == "no":
        print("Alright then. If you say so...")
        break


print("\n===================")
print("!!! Let's Begin !!!")
print("===================\n")

# Difficulty selection / asks user what diff...
ask_diff = difficult("What difficulty would you like? ")

if ask_diff == "easy":
    difficulty = "easy"

elif ask_diff == "medium":
    difficulty = "medium"

elif ask_diff == "hard":
    difficulty = "hard"

# Outputs the selected difficulty
print(f"You've selected the {ask_diff} difficulty")
print()

# Variables that are placeholders of round mechanics
rounds_played = 0
rounds_won = 0
rounds_lost = 0

# guesses given and list
guesses_given = 3
already_guessed = []

# Asks user how many rounds they want to play...
while True:

    rounds = int_checker("How many rounds (<ENTER> for infinite): ")

    if rounds == "xxx":
        print("Please play at least one round.\n")

    else:
        break

# Looping mechanics for rounds
end_game = "no"
while True:

    # Selects the heading, depending on if user is playing continuous mode or not
    if rounds == "":
        print()
        heading = f"Round {rounds_played + 1} of Continuous Mode"

    else:
        print()
        heading = f"Round {rounds_played + 1} of {rounds}"

    # Displays the heading after each question
    print(heading)

    if difficulty == "easy":
        a_side = random.randint(1, 10)
        o_side = random.randint(1, 10)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                    f"Answer: {round(answer_h, 1)} "

        # the actual answer, used for comparison, rounded to 1 decimal point
        answer = round(answer_h, 1)

        # loops as long as the user still has guesses remaining
        while guesses_given > 0:

            guess = guess_float_checker(quest_ask)

            # prevents user from inputting the same guess, does not use a guess
            if guess in already_guessed:
                print("You've already guessed that number...\n")
                continue

            # compares the answer to users guess and outputs appropriate response, adds a round won to stats
            if guess == answer:
                rounds_won += 1
                print(f"Congratulations! You got the answer with {guesses_given - 1} guess(es) remaining.\n")
                break

            elif guess == "xxx":
                end_game = "yes"
                break

            # if the user gets it wrong
            else:
                guesses_given -= 1
                print(f"You've guessed incorrectly, {guesses_given} guess(es) remaining. Try Again.\n")

            # places the users guesses in a list
            already_guessed.append(guess)

            # ends game one user runs out of guesses, adds a round
            if guesses_given == 0:
                rounds_lost += 1
                print("You've run out of guesses. Game Over.")
                continue

        # Keeps track of how many rounds the player has played, adds one once they finish (win or lose)
        rounds_played += 1

        # Ends game once user has run out of answers / guesses / attempts or if user uses exit code
        if rounds_played == rounds or end_game == "yes":
            break

# Displays the history

# Statistics - shows win/lose percentages

percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print("\n*** Game Statistics ***")
print(f"You won {percent_win:.1f}% and lost {percent_lose:.1f}% of the rounds.")

# Thanks the user for playing the quiz
print("Thanks for playing!")

# testing...
print("Rounds: ", rounds)
print("Played: ", rounds_played)
print("Won: ", rounds_won)
print("Lost: ", rounds_lost)
