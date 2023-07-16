import math
import random


def float_checker(question):
    while True:
        response = input(question)
        error = "Please enter a valid number (only 1 d.p)"
        if response != "":
            try:
                response = float(response)
                if response < 1:
                    print(error)
                    continue
            except ValueError:
                print(error)
                continue
        return response


# Set the difficulty to replace difficulty component (testing purposes)
difficulty = input("Difficulty: ")

if difficulty == "easy":
    a_side = random.randint(1, 10)
    o_side = random.randint(1, 10)
    answer_h = math.sqrt(a_side ** 2 + o_side ** 2)
    quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

    answer = round(answer_h, 1)
    guess = float_checker(quest_ask)

    if guess == answer:
        print("Congratulations! You got the answer.")
    else:
        print(f"Wrong answer. The correct answer is {answer}.")
    print()

elif difficulty == "medium":
    a_side = random.randint(10, 20)
    o_side = random.randint(10, 20)
    answer_h = math.sqrt(a_side ** 2 + o_side ** 2)
    quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "

    guess = float_checker(quest_ask)
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
        quest_ask = f"If the hypotenuse is {round(answer_h, 1)} and the opposite is {o_side}, what is the adjacent? "
        answer = round(a_side, 1)

    elif random_side == "opposite":
        quest_ask = f"If the hypotenuse is {round(answer_h)} and the adjacent is {a_side}, what is the opposite? "
        answer = round(o_side, 1)

    else:
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? "
        answer = round(answer_h, 1)

    guess = float_checker(quest_ask)
    if guess == answer:
        print("Congratulations! You got the answer.")
    else:
        print(f"Wrong answer. The correct answer is {answer}.")
    print()
