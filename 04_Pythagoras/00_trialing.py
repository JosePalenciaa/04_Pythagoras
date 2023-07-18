import math
import random


# Functions go here...


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

# list for accepted values of difficulty
diff_list = ["easy", "medium", "hard"]

difficulty = ""

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

    # guesses given and list, placed in loop so it resets when a new round starts
    guesses_given = 3
    already_guessed = []

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
                break

        # Keeps track of how many rounds the player has played, adds one once they finish (win or lose)
        rounds_played += 1

        # Ends game once user has run out of answers / guesses / attempts or if user uses exit code
        if rounds_played == rounds or end_game == "yes":
            break

    elif difficulty == "medium":
        a_side = random.randint(10, 20)
        o_side = random.randint(10, 20)
        answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

        # Answer given for testing purposes...
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                    f"Answer: {round(answer_h, 1)} "

        answer = round(answer_h, 1)

        while guesses_given > 0:

            guess = guess_float_checker(quest_ask)

            if guess in already_guessed:
                print("You've already guessed that number...\n")
                continue

            if guess == answer:
                rounds_won += 1
                print(f"Congratulations! You got the answer with {guesses_given - 1} guess(es) remaining.\n")
                break

            elif guess == "xxx":
                end_game = "yes"
                break

            else:
                guesses_given -= 1
                print(f"You've guessed incorrectly, {guesses_given} guess(es) remaining. Try Again.\n")

            already_guessed.append(guess)

            if guesses_given == 0:
                rounds_lost += 1
                print("You've run out of guesses. Round Over.")
                continue

        rounds_played += 1

        if rounds_played == rounds or end_game == "yes":
            break

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
            quest_ask = f"If the hypotenuse is {round(answer_h, 1)} and the adjacent is {a_side}, what is the opposite? " \
                        f"Answer: {round(o_side, 1)} "
            answer = round(o_side, 1)

        else:
            quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                        f"Answer: {round(answer_h, 1)} "
            answer = round(answer_h, 1)

        while guesses_given > 0:

            guess = guess_float_checker(quest_ask)

            if guess in already_guessed:
                print("You've already guessed that number...\n")
                continue

            if guess == answer:
                rounds_won += 1
                print(f"Congratulations! You got the answer with {guesses_given - 1} guess(es) remaining.\n")
                break

            elif guess == "xxx":
                end_game = "yes"
                break

            else:
                guesses_given -= 1
                print(f"You've guessed incorrectly, {guesses_given} guess(es) remaining. Try Again.\n")

            if guesses_given == 0:
                rounds_lost += 1
                print("You've run out of guesses. Game Over.")
                break

        rounds_played += 1

        if rounds_played == rounds or end_game == "yes":
            break


# Shows game statistics once user has finished round(s)

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
