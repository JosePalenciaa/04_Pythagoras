import math
import random


# Functions go here...

# Displays instructions function
def instructions():
    print("---------------------")
    print("**** How to Play ****")
    print("---------------------")
    print()
    print("Your goal is to calculate the missing side using the 'Pythagoras Theorem'..."
          "\n• Formulas:\n\tHypotenuse | a² + b² = c²\n\tOpposite | c² - a² = b²\n\tAdjacent | c² - b² = a²"
          "\n\tHypotenuse = c | Opposite / Adjacent = b / a"
          "\n\n• First select a difficulty."
          "\n• You are given 3 attempts. "
          "\n• Solve the missing side. "
          "\n• Round your answer to whole integers."
          "\n• Can you win?")
    print()


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


# checks to see if user input is a valid number, if <ENTER> gives output
def guess_int_checker(question):
    while True:
        response = input(question)

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
diff_list = ["easy", "medium", "hard", "xxx"]

difficulty = ""

# Main Routine goes here...

# Introduction / title of game
print("######################################")
print("!!! Welcome to the Pythagoras Quiz !!!")
print("######################################")
print()

# Looping to so user response of 'why' outputs statement, and reruns the question
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

# Asks user how many rounds they want to play...
rounds = int_checker("How many rounds (<ENTER> for infinite): ")

# Looping mechanics for rounds
end_game = "no"
while rounds != "xxx":

    if difficulty == "easy":
        a_side = random.randint(1, 10)
        o_side = random.randint(1, 10)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                    f"Answer: {round(answer_h, 1)} "

        answer = round(answer_h, 1)
        guess = guess_int_checker(quest_ask)

        if guess == answer:
            print("Congratulations! You got the answer.")
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
        print()

    elif difficulty == "medium":
        a_side = random.randint(10, 20)
        o_side = random.randint(10, 20)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                    f"Answer: {round(answer_h, 1)} "

        guess = guess_int_checker(quest_ask)
        answer = round(answer_h, 1)

        if guess == answer:
            print("Congratulations! You got the answer.")
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
        print()

    elif difficulty == "hard":
        sides = ["adjacent", "opposite", "hypotenuse"]

        random_side = random.choice(sides)
        a_side = random.randint(10, 20)
        o_side = random.randint(10, 20)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Answer given for testing purposes
        if random_side == "adjacent":
            quest_ask = f"If the hypotenuse is {round(answer_h, 1)} and the opposite is {o_side}, what is the adjacent?" \
                        f" Answer: {round(a_side, 1)} "
            answer = round(a_side, 1)

        elif random_side == "opposite":
            quest_ask = f"If the hypotenuse is {round(answer_h)} and the adjacent is {a_side}, what is the opposite? " \
                        f"Answer: {round(o_side, 1)} "
            answer = round(o_side, 1)

        else:
            quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                        f"Answer: {round(answer_h, 1)} "
            answer = round(answer_h, 1)

        guess = guess_int_checker(quest_ask)
        if guess == answer:
            print("Congratulations! You got the answer.")
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
        print()

    # Guess(es) value and already guessed list...
    guesses_given = 3
    already_guessed = []

    # Guesses mechanics go here...

    # ends game when user plays all rounds
    if rounds_played == rounds:
        break
