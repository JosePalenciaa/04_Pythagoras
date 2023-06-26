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


a_side = random.randint(1, 10)
o_side = random. randint(1, 10)
h_side = math.sqrt(a_side ** 2 + o_side ** 2)
answer = round(h_side)

# substitute for difficulty checker...
difficulty = "easy"

while True:

    guess = int_checker(f"What is the hypotenuse of if the adjacent is {a_side} and the opposite is {o_side}? ")

    if difficulty == "easy":

        if guess == answer:
            print("Congratulations! You got the answer.")

        else:
            print("Wrong answer")
