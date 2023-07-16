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

        error = "Please enter a valid integer\n"

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
def answer_float_checker(question):
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

# Introduction / title of the quiz
print("######################################")
print("!!! Welcome to the Pythagoras Quiz !!!")
print("######################################")
print()

# Looping so user response, 'why', gives the response, and asks the question again
while True:
    # Asks user for a response (related to the instructions)
    display_instructions = yes_no_why("Do you want to see the INSTRUCTIONS (y / n / w)? ")

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

# Title labeling the start of the quiz
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

# Variables that are placeholders for round mechanics
rounds_played = 0
rounds_won = 0
rounds_lost = 0

# Asks user how many rounds they want to play...
while True:

    # Asks the user how many rounds they want to play, or if they want infinite rounds
    rounds = int_checker("How many rounds (<ENTER> for infinite): ")

    # Makes the user play at least 1 round when they try quiting prematurely
    if rounds == "xxx":
        print("Please play at least one round.\n")

    # If the users input != "xxx" the loop breaks and the program continues
    else:
        break

# Looping mechanics for rounds
end_quiz = "no"
while True:

    # Selects the heading, depending on if user is playing INFINITE mode or not
    if rounds == "":
        print()
        heading = f"Round {rounds_played + 1} of INFINITE Mode"

    else:
        print()
        heading = f"Round {rounds_played + 1} of {rounds}"

    # Displays the heading after each question
    print(heading)

    # Attempts given and list, placed in a loop - resets when a new round starts
    attempts_given = 3
    already_attempted = []

    # Side values and answer the difficulty is "Easy"
    if difficulty == "easy":
        a_side = random.randint(1, 10)
        o_side = random.randint(1, 10)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Question which the user is asked in easy difficulty
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

        # The actual answer, used for comparison, rounded to 1 decimal point
        answer = round(answer_h, 1)

    # Side values and answer the difficulty is "Medium"
    elif difficulty == "medium":
        a_side = random.randint(10, 20)
        o_side = random.randint(10, 20)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Question which user is asked in medium difficulty
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

        answer = round(answer_h, 1)

    # Side values and answer the difficulty is "Hard"
    elif difficulty == "hard":

        # Randomly selects a side to generate a question related to it
        sides = ["adjacent", "opposite", "hypotenuse"]
        random_side = random.choice(sides)

        a_side = random.randint(10, 20)
        o_side = random.randint(10, 20)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Questions - determined by which side was chosen above
        if random_side == "adjacent":
            quest_ask = f"If the hypotenuse is {round(answer_h, 1)} and the opposite is {o_side}, what is the adjacent? "
            answer = round(a_side, 1)

        elif random_side == "opposite":
            quest_ask = f"If the hypotenuse is {round(answer_h, 1)} and the adjacent is {a_side}, what is the opposite? "
            answer = round(o_side, 1)

        else:
            quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

            answer = round(answer_h, 1)

    # Loop that continues while user still has attempts
    while attempts_given > 0:

        # Gets users answer to the question
        user_answer = answer_float_checker(quest_ask)

        # If user has guessed the same number, tell them - does not take a guess
        if user_answer in already_attempted:
            print("You've already tried that number...\n")
            continue

        # Compares users answer to the real answer, if they get it right, congratulate them - add +1 to rounds won
        if user_answer == answer:
            rounds_won += 1
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

        # If the user runs out of attempts, ends the round
        if attempts_given == 0:
            rounds_lost += 1
            print("You've run out of attempts. Round Over.")
            break

    # Once loop finishes, a round also finishes
    rounds_played += 1

    # Ends the quiz if user plays all rounds or inputs the exit code
    # Different outputs because of two different scenarios

    if rounds_played == rounds:
        print("\nAll rounds have been completed.")
        break

    elif end_quiz == "yes":
        print("\nYou have chosen to end the quiz, no round(s).")
        break

# Shows quiz statistics once user has finished round(s)...

# Gives the percentage forms of rounds won, lost, and not played (all rounded to 1 dp)
percent_win = round(rounds_won / rounds_played * 100, 1)
percent_lose = round(rounds_lost / rounds_played * 100, 1)
percent_not_played = round(100 - percent_lose - percent_win, 1)

print("\n**** quiz Statistics ****")
# Changes depending on if user selected a set value, or infinite rounds
if rounds == "":
    print(f"Round(s) selected: INFINITE")

else:
    print(f"Round(s) selected: {rounds}")

# Percentages - win / lose / not played
print(f"You won: {rounds_won} round(s), {percent_win}%")
print(f"You lost: {rounds_lost} round(s), {percent_lose}%")
print(f"You didn't play: {rounds_played - rounds_lost - rounds_won} round(s), {percent_not_played}%")

# Thanks the user for playing the quiz
print("\nThanks for playing!")
