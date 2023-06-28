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


# Lists go here...

# list of accepted values for yes / no checker
yesno_list = ["yes", "no", "why"]

# list for accepted values of difficulty
diff_list = ["easy", "moderate", "hard", "xxx"]

# Main Routine goes here...

# Introduction / title of game
print("######################################")
print("!!! Welcome to the Pythagoras Quiz !!!")
print("######################################")
print()

# Asks user for a response (related to the instructions)
display_instructions = yes_no_why("Do you want to see Instructions? ")

# Displays instructions of user says 'yes'
if display_instructions == "yes":
    print()
    instructions()

# Gets angry at user if they respond with 'why'
elif display_instructions == "why":
    print("Because I said so!!!")

print("\n===================")
print("!!! Let's Begin !!!")
print("===================\n")

# Variables that are placeholders of round mechanics
rounds_played = 0
rounds_won = 0
rounds_lost = 0

# Asks user how many rounds they want to play...
rounds = int_checker("How many rounds (<ENTER> for infinite): ")

# Looping mechanics for rounds
end_game = "no"
while rounds != "xxx":

    # If user inputs <ENTER>, there are infinite rounds
    if rounds == "":
        print()
        heading = f"Round {rounds_played + 1} of Continuous Mode"

    else:
        print()
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)
    choose = input(f"Enter a number or 'xxx' to end: ")
    rounds_played += 1

    if rounds_played == rounds:
        break