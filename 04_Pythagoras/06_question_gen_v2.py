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


# difficulty set to "easy" for trialing
difficulty = "easy"

a_side = 0
o_side = 0
answer_h = 0

if difficulty == "easy":
    a_side = random.randint(1, 10)
    o_side = random.randint(1, 10)
    answer_h = math.sqrt(round(a_side ** 2 + o_side ** 2))

elif difficulty == "medium":
    a_side = random.randint(10, 20)
    o_side = random.randint(10, 20)
    answer_h = math.sqrt(round(a_side ** 2 + o_side ** 2))

# when difficulty == "hard":
else:
    a_side = random.randint(10, 20)
    o_side = random.randint(10, 20)
    answer_h = math.sqrt(round(a_side ** 2 + o_side ** 2))

# Looping for testing purposes
