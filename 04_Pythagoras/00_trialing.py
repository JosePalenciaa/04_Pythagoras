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
          "\n\n• First select a difficulty (easy / medium / hard)."
          "\n• You are given 3 attempts - Answer with 'xxx' to end quiz. "
          "\n• Solve the missing side. "
          "\n• Hypotenuse should be rounded to 1dp | Adjacent and opposite to integers."
          "\n• How smart do you think you are?")


# Number checker function - given the situation, the user can input both integers and floats, or exclusively integers
def number_checker(question, allow_floats="yes"):

    # Looping that continues until the user inputs a valid response to the question
    while True:
        response = input(question)

        # Used as the exit code
        if response == "xxx":
            return response

        # When the user does not input <ENTER> / when they select infinite mode
        elif response != "":
            try:
                # Allows floats (numbers and integers) - Used to check if the user inputs a valid answer
                if allow_floats == "yes":
                    response = float(response)

                    # When implemented into base, no sides (which the user has to find) will be less than 1
                    if response < 1:
                        print("Please input a valid NUMBER (> 1)\n")
                        continue

                # Allows only integers - Used to select and validate the # of questions
                elif allow_floats == "no":
                    response = int(response)

                    if response < 1:
                        print("Please input a valid integer (> 0)\n")
                        continue

            # Outputs an error when the user inputs 'something' that would cause a ValueError
            except ValueError:
                print("<ValueError> That is an invalid INTEGER / NUMBER\n")
                continue

        return response


# User input function - uses one function to get the users input for the difficulty and for the instructions
def user_input(question, valid_lists, error):
    while True:
        response = input(question).lower()

        # Searches and checks the list (depending on the question) for valid responses, otherwise prints an error
        for item in valid_lists:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Function used to make the game look good
def statement_generator(statement, decoration, above_below, has_emoji=None):
    sides = decoration * 3

    # statement = "{} {} {}".format(sides, statement, sides)
    statement = f"{sides} {statement} {sides}"

    if has_emoji == "yes":
        top_bottom_length = len(statement) + (len(sides) * 2) + 2
    else:
        top_bottom_length = len(statement)

    top_bottom = above_below * top_bottom_length

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Lists go here...

# list of accepted values when asked if the user wants to see the instructions
yesno_list = ["yes", "no", "why"]

# list for accepted values when the user is asked what difficulty they want
diff_list = ["easy", "medium", "hard"]

difficulty = ""

# Main Routine goes here...

# Introduction / title of the quiz
statement_generator("Welcome to the Pythagoras Quiz", "📐", "=", "yes")
print()

# Loop so if the user inputs "why", the program gives an output and asks again, until user inputs "y" / "n"
while True:
    # Asks user for a response (related to the instructions)
    display_instructions = user_input("Do you want to see the INSTRUCTIONS (yes / no / why)? "
                                      , yesno_list, "Please enter a valid response (y / n / w)")

    # Gets angry at user if they respond with 'why', loop continues
    if display_instructions == "why":
        print("Because I said so!!!")
        print()
        continue

    # Displays instructions of user says 'yes', loop breaks and continues with rest of program
    elif display_instructions == "yes":
        print()
        instructions()
        break

    # Outputs a statement if user says 'no', loop breaks and continues with rest of code, does not display instructions
    else:
        print("Alright then. If you say so...")
        break

# Title that labels the start of the quiz
print()
statement_generator("Lets Begin", "!", "=", "no")
print()

# Difficulty selection / asks user what difficulty then want to select
# Checks the diff_list and outputs an error if user inputs an invalid difficulty
difficulty = user_input("What difficulty would you like (easy / medium / hard)? ", diff_list,
                        "Please enter a valid difficulty (e / m / h)")

# Tells the user what difficulty they have selected
print()
statement_generator(f"You've selected the {difficulty.upper()} difficulty", "|", "-", "no")
print()

# Variables that are placeholders for questions mechanics
answered_questions = 0
questions_correct = 0
questions_incorrect = 0

# Asks user how many questions the user wants to attempt...
# Loop that makes it so the user has to attempt at least one question
while True:

    # Asks the user how many questions they want to attempt, or if they want infinite questions
    # Checks to see if the user inputs an integer (does not allow floats - will print an error)
    questions_amount = number_checker("How many questions (<ENTER> for infinite): ", allow_floats="no")

    # Makes the user attempt at least 1 question when they try exiting prematurely
    if questions_amount == "xxx":
        print("Please attempt at least one question.\n")

    # If the users input = "y" or "n" it is accepted - the loop breaks and the rest of the program continues
    else:
        break

# Looping mechanics for questions, and ends quiz when user chooses to
end_quiz = "no"
while True:

    if difficulty == "easy":
        x = random.randint(3, 10)
        odd_even = x % 2

        if odd_even == 0:
            a = x
            b = int((x / 2) ** 2 - 1)
            c = (x / 2) ** 2 + 1

        else:
            a = x
            b = int((x ** 2 / 2) - 0.5)
            c = (x ** 2 / 2) + 0.5

        # Question which the user is asked in easy difficulty
        quest_ask = f"If the adjacent is {x} (a) and the opposite is {b} (b), what is the hypotenuse (c)? "

        # The actual answer, used for comparison to see if they get it correct or incorrect
        answer = c

    # Generates side values and answer when the difficulty is "Medium"
    else:
        a_side, o_side = random.randint(10, 20), random.randint(10, 20)
        hypotenuse = math.sqrt(a_side ** 2 + o_side ** 2)

        if difficulty == "medium":
            # Question which user is asked in medium difficulty
            quest_ask = f"If the adjacent is {a_side} (a) and the opposite is {o_side} (b), what is the hypotenuse (c)? "

            answer = round(hypotenuse, 1)

        # Generates side values and answer when the difficulty is "Hard"
        elif difficulty == "hard":

            # Randomly selects a side to generate a question related to it
            sides = ["adjacent", "opposite", "hypotenuse"]
            random_side = random.choice(sides)

            # Questions - determined by which side was chosen above
            if random_side == "adjacent":
                quest_ask = f"If the hypotenuse is {round(hypotenuse, 1)} (c) and the opposite is {o_side} (b), " \
                            f"what is the adjacent (a)? "
                answer = round(a_side, 1)

            elif random_side == "opposite":
                quest_ask = f"If the hypotenuse is {round(hypotenuse, 1)} (c) and the adjacent is {a_side} (a), " \
                            f"what is the opposite (b)? "
                answer = round(o_side, 1)

            else:
                quest_ask = f"If the adjacent is {a_side} (a) and the opposite is {o_side} (b), " \
                            f"what is the hypotenuse (h)? "

                answer = round(hypotenuse, 1)
