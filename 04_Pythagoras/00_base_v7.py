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


# Lists go here...

# list of accepted values when asked if the user wants to see the instructions
yesno_list = ["yes", "no", "why"]

# list for accepted values when the user is asked what difficulty they want
diff_list = ["easy", "medium", "hard"]

difficulty = ""

# Main Routine goes here...

# Introduction / title of the quiz
print("######################################")
print("!!! Welcome to the Pythagoras Quiz !!!")
print("######################################")
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
print("\n===================")
print("!!! Let's Begin !!!")
print("===================\n")

# Difficulty selection / asks user what difficulty then want to select
# Checks the diff_list and outputs an error if user inputs an invalid difficulty
difficulty = user_input("What difficulty would you like (easy / medium / hard)? ", diff_list,
                        "Please enter a valid difficulty (e / m / h)")

# Tells the user what difficulty they have selected
print(f"\nYou've selected the {difficulty} difficulty\n")

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

    # Selects the heading, depending on if user is attempting INFINITE mode or not
    if questions_amount == "":
        print()
        heading = f"Question {answered_questions + 1} of INFINITE Mode"

    else:
        print()
        heading = f"Question {answered_questions + 1} of {questions_amount}"

    # Displays the heading after each question
    print(heading)

    # Number of attempts given, and already attempted list, placed in a loop - resets when a new question starts
    attempts_given = 3
    already_attempted = []

    # Generates side values and answer when the difficulty is "Easy"
    if difficulty == "easy":
        a_side = random.randint(1, 10)
        o_side = random.randint(1, 10)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Question which the user is asked in easy difficulty
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

        # The actual answer, used for comparison to see if they get it right or wrong, rounded to 1 decimal point
        answer = round(answer_h, 1)

    # Generates side values and answer when the difficulty is "Medium"
    elif difficulty == "medium":
        a_side = random.randint(10, 20)
        o_side = random.randint(10, 20)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Question which user is asked in medium difficulty
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

        answer = round(answer_h, 1)

    # Generates side values and answer when the difficulty is "Hard"
    elif difficulty == "hard":

        # Randomly selects a side to generate a question related to it
        sides = ["adjacent", "opposite", "hypotenuse"]
        random_side = random.choice(sides)

        a_side = random.randint(10, 20)
        o_side = random.randint(10, 20)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Questions - determined by which side was chosen above
        if random_side == "adjacent":
            quest_ask = f"If the hypotenuse is {round(answer_h, 1)} and the opposite is {o_side}, " \
                        f"what is the adjacent? "
            answer = round(a_side, 1)

        elif random_side == "opposite":
            quest_ask = f"If the hypotenuse is {round(answer_h, 1)} and the adjacent is {a_side}, " \
                        f"what is the opposite? "
            answer = round(o_side, 1)

        else:
            quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

            answer = round(answer_h, 1)

    # Loop that continues while user still has attempts
    while attempts_given > 0:

        # Gets users answer to the question
        user_answer = number_checker(quest_ask, allow_floats="yes")

        # If user has answered the same number, tell them - does not take remove an attempt from their given amount
        if user_answer in already_attempted:
            print("You've already tried that number...\n")
            continue

        # Does not allow <ENTER> for an answer, incase user accidentally presses enter twice-3
        if user_answer == "":
            print("<ENTER> IS NOT AN ACCEPTED ANSWER!\n")
            continue

        # Compares users answer to the real answer, if they get it right, congratulate them - add +1 to questions
        # that the user has correctly answered
        elif user_answer == answer:
            questions_correct += 1
            print(f"Congratulations! You got the answer with {attempts_given - 1} attempt(s) remaining.\n")
            break

        # Ends quiz if user inputs exit code
        elif user_answer == "xxx":
            end_quiz = "yes"
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

    # Once loop finishes, the program keeps track of the number of questions which the user has answered
    answered_questions += 1

    # Ends the quiz if user answers all questions or inputs the exit code
    # Different outputs because of two different scenarios

    if answered_questions == questions_amount:
        print("\nAll questions have been answered.")
        break

    elif end_quiz == "yes":
        print("\nYou have chosen to end the quiz, no more question(s).")
        break

# Shows quiz statistics once user has finished the question(s)...

# Gives the percentage forms of question(s) answered correctly, incorrectly, and not answered (all rounded to 1 dp)
percent_correct = round(questions_correct / answered_questions * 100, 1)
percent_incorrect = round(questions_incorrect / answered_questions * 100, 1)
percent_not_answered = round(100 - percent_incorrect - percent_correct, 1)

print("\n**** quiz Statistics ****")
# Changes depending on if user selected a set value, or infinite questions
if questions_amount == "":
    print(f"Question(s) selected: INFINITE questions")

else:
    print(f"Question(s) selected: {questions_amount} question(s)")

# Percentages - Correct / Incorrect / Unanswered
print("\nOf the questions you've answered (including 'xxx')-3x: ")
print(f"You didn't answer: {answered_questions - questions_incorrect - questions_correct} question(s), "
      f"{percent_not_answered}%")
print(f"Correct: {questions_correct} question(s), {percent_correct}%")
print(f"Incorrect: {questions_incorrect} question(s), {percent_incorrect}%")

# Thanks the user for playing the quiz
print("\nThanks for playing!")
