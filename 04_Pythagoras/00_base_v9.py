import math
import random


# Functions go here...

# Displays instructions function (depends on the users input of y / n / w / etc...)
def instructions():
    print("\n---------------------")
    print("**** How to Play ****")
    print("---------------------")
    print("\nYour goal is to calculate the missing side using the 'Pythagorean Theorem'..."
          "\n• Formulas:\n\tHypotenuse | a² + b² = c²\n\tOpposite | c² - a² = b²\n\tAdjacent | c² - b² = a²"
          "\n\tHypotenuse = c | Opposite / Adjacent = b / a"
          "\n\n• First select a difficulty (easy / medium / hard)."
          "\n• You are given 3 attempts - Answer with 'xxx' to end quiz (except on the first attempt, first question. "
          "\n• Solve the missing side. "
          "\n• Hypotenuse should be rounded to 1dp | Adjacent and opposite to integers."
          "\n• How smart do you think you are?")


# Number checker function - given the situation, the user can input both integers and floats, or exclusively integers
def number_checker(question, allow_floats=False):
    # Looping that continues until the user inputs a valid response to the question
    while True:
        response = input(question)

        # Detects the exit code, depending on which part of the program it is detected, an appropriate output is given
        if response == "xxx":
            return response

        # When the user does not input <ENTER> / when they select infinite mode...
        elif response != "":
            try:
                # Allows floats (numbers and integers) - Used to check if the user inputs a valid answer
                if allow_floats is True:
                    response = float(response)

                    # Doesn't allow any values less than 0 / values that are negative
                    if response <= 0:
                        print("Please input a valid NUMBER (> 0)\n")
                        continue

                # Allows only integers - Used to select and validate the # of questions
                elif allow_floats is False:
                    response = int(response)

                    # The lowest amount of questions possible is 1, hence the error when user inputs less than 1
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

        # Prints the appropriate error depending on which question was asked (difficulty or yes / no)
        print(error + '\n')


# Function used to make the game look good / for the aesthetics, makes the heading / subheadings 'unique'
def statement_generator(statement, decoration, above_below, has_emoji=None):
    sides = decoration * 3

    # statement = "{} {} {}".format(sides, statement, sides)
    statement = f"{sides} {statement} {sides}"

    # If the statement has emojis, the lengths of the decoration is calculated differently compared to without
    if has_emoji == "yes":
        top_bottom_length = len(statement) + (len(sides) * 2) + 2
    else:
        top_bottom_length = len(statement)

    top_bottom = above_below * top_bottom_length

    # Displays the statement with the decoration
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return


# Main Routine goes here...

# Lists go here...

# list of accepted values when asked if the user wants to see the instructions
yesno_list = ["yes", "no", "why"]

# list for accepted values when the user is asked what difficulty they want
diff_list = ["easy", "medium", "hard"]

# Introduction / title of the quiz, contains emojis, hence allowing emojis
statement_generator("Welcome to the Pythagoras Quiz", "📐", "=", "yes")
print()

# Loop so if the user inputs "why", the program gives an output and asks again, until user inputs "y" / "n"
while True:
    # Asks user for a response (related to the instructions)
    display_instructions = user_input("Do you want to see the INSTRUCTIONS (yes / no / why)? ",
                                      yesno_list, "Please enter a valid response (y / n / w)")

    # Gets angry at user if they respond with 'why', loop repeats until user inputs "y" / "n"
    if display_instructions == "why":
        print("Because I said so!!!\n")

        continue

    # Displays instructions of user says 'yes', loop breaks and continues with rest of program
    elif display_instructions == "yes":
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
    # Checks to see if the user inputs an integer (does not allow floats (cannot have decimal rounds)
    questions_amount = number_checker("How many questions (<ENTER> for infinite): ")

    # Makes the user attempt at least 1 question when they try exiting prematurely
    if questions_amount == "xxx":
        print("Please attempt at least one question.\n")

    # If the users input = "y" or "n" it is accepted - the loop breaks and the rest of the program continues
    else:
        break

# Looping mechanics for questions, and ends quiz when user chooses to
end_quiz = "no"
while end_quiz != "yes":

    # Adds +=1 the answered_questions variable, this keeps track of the amount of questions user has answered
    answered_questions += 1

    # call variables
    quest_ask = ""
    answer = ""

    # Selects the heading, depending on if user is attempting INFINITE mode or not
    if questions_amount == "":
        heading = f"\nQuestion {answered_questions} of INFINITE Mode:"

    else:
        heading = f"\nQuestion {answered_questions} of {questions_amount}:"

    # Displays the heading after each question
    print(heading)

    # Number of attempts given, and already attempted list, placed in a loop - resets when a new question starts
    attempts_given = 3
    already_attempted = []

    # Generates side values and answer when the difficulty is "Easy"
    # Sides are generated using the formula for Pythagorean triples, which only needs 1 side value
    # different formulas are used, depending on if it is even or odd
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
        quest_ask = f"If the adjacent is {x} and the opposite is {b}, what is the hypotenuse (c)? "

        # The actual answer, used for comparison to see if they get it correct or incorrect
        answer = c

    # Generates the side values for "medium" and "hard" difficulties
    # The questions vary, depending on the difficulty
    else:
        a_side, o_side = random.randint(10, 20), random.randint(10, 20)
        hypotenuse = math.sqrt(a_side ** 2 + o_side ** 2)

        if difficulty == "medium":
            # Question which user is asked in medium difficulty
            quest_ask = f"If the adjacent is {a_side} (a) and the " \
                        f"opposite is {o_side} (b), what is the hypotenuse (c)? "

            answer = round(hypotenuse, 1)

        # Hard mode uses the same values as medium mode but has 3 possible questions, rather than just the hypotenuse
        elif difficulty == "hard":

            # Randomly selects a side to generate a question related to it
            random_side = random.choice(["adjacent", "opposite", "hypotenuse"])

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

    # Loop that continues while user still has attempts
    while attempts_given > 0:

        # Gets users answer to the question (allows floats because the user can input floats as answers)
        user_answer = number_checker(quest_ask, True)

        # If the user tries to quit on their first attempt of their first question, it prevents them
        # User cannot exit on first question and first attempt
        if user_answer == "xxx" and answered_questions == 1 and attempts_given == 3:
            print("PLEASE ATTEMPT AT LEAST ONE QUESTION!!! 😡😡😡\n")
            continue

        # Ends quiz if user inputs exit code
        elif user_answer == "xxx":
            end_quiz = "yes"
            break

        # If user has answered the same number, tell them - does not take remove an attempt from their given amount
        if user_answer in already_attempted:
            print("You've already tried that number...\n")
            continue

        # Does not allow <ENTER> for an answer, incase user accidentally presses enter twice-3
        elif user_answer == "":
            print("<ENTER> IS NOT AN ACCEPTED ANSWER!\n")
            continue

        # Compares users answer to the real answer, if they get it correct, congratulate them - add +1 to questions
        # that the user has correctly answered
        elif user_answer == answer:
            questions_correct += 1
            print(f"Congratulations! You got the answer with {attempts_given - 1} attempt(s) remaining.\n")
            break

        # If users answer is incorrect, tell them and remove 1 attempt from the 3 given
        else:
            attempts_given -= 1
            print(f"You've answered incorrectly, {attempts_given} attempt(s) remaining. Try Again.\n")

            # places the users attempts in a list - used to check for duplicates
            already_attempted.append(user_answer)

        # If the user runs out of attempts, ends the question ends
        if attempts_given == 0:
            questions_incorrect += 1
            print(f"You've run out of attempts: The answer was {answer}. Question Over.")
            break

    # Ends the quiz if user answers all questions or inputs the exit code
    # Different outputs because of two different scenarios
    if answered_questions == questions_amount:
        print("\nAll questions have been attempted.")
        break

# Shows quiz statistics once user has finished the question(s)...
# Gives the percentage forms of question(s) answered correctly, incorrectly, and not answered (all rounded to 1 dp)
percent_correct = round(questions_correct / answered_questions * 100, 1)
percent_incorrect = round(questions_incorrect / answered_questions * 100, 1)
percent_not_answered = round(100 - percent_incorrect - percent_correct, 1)

print()
statement_generator("Quiz Statistics", "*", "=", "no")
print()

# Changes depending on if user selected a set value for how many questions, or infinite questions
if questions_amount == "":
    print(f"Question(s) selected: INFINITE questions")
    print(f"Questions answered: {answered_questions}")

else:
    print(f"Question(s) selected: {questions_amount} question(s)")

# Percentages - Correct / Incorrect / Unanswered
print("\nOf the questions you've answered (including 'xxx'): ")
print(f"You didn't answer: {answered_questions - questions_incorrect - questions_correct} question(s), "
      f"{percent_not_answered}%")
print(f"Correct: {questions_correct} question(s), {percent_correct}%")
print(f"Incorrect: {questions_incorrect} question(s), {percent_incorrect}%")

# Thanks the user for playing the quiz
print("\nThanks for playing!")
