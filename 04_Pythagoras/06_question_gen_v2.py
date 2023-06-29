import math
import random


def int_checker(question):
    while True:
        response = input(question)
        error = "Please enter a valid integer"
        if response != "":
            try:
                response = int(response)
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
    answer_h = math.sqrt(round(a_side ** 2 + o_side ** 2))
    quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                f"Answer: {round(answer_h)} "

    answer = round(answer_h)
    guess = int_checker(quest_ask)

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
                f"Answer: {round(answer_h)} "

    guess = int_checker(quest_ask)
    answer = round(answer_h)

    if guess == answer:
        print("Congratulations! You got the answer.")
    else:
        print(f"Wrong answer. The correct answer is {answer}.")
    print()

elif difficulty == "hard":
    sides = ["adjacent", "opposite", "hypotenuse"]

    # had to ask chat gpt how to loop...
    random_side = random.choice(sides)
    a_side = random.randint(10, 20)
    o_side = random.randint(10, 20)
    answer_h = math.sqrt(a_side ** 2 + o_side ** 2)

    # Answer given for testing purposes
    if random_side == "adjacent":
        quest_ask = f"If the hypotenuse is {round(answer_h, 2)} and the opposite is {o_side}, what is the adjacent? " \
                    f"Answer: {round(a_side)} "
        answer = round(a_side)

    elif random_side == "opposite":
        quest_ask = f"If the hypotenuse is {round(answer_h, 2)} and the adjacent is {a_side}, what is the opposite? " \
                    f"Answer: {round(o_side)} "
        answer = round(o_side)

    else:
        quest_ask = f"If the adjacent is {a_side} and the opposite is {o_side}, what is the hypotenuse? " \
                    f"Answer: {round(answer_h)} "
        answer = round(answer_h)

    guess = int_checker(quest_ask)
    if guess == answer:
        print("Congratulations! You got the answer.")
    else:
        print(f"Wrong answer. The correct answer is {answer}.")
    print()
