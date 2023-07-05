import random
import math
# Questions change depending on difficulty...


def difficult(question):
    while True:
        response = input(question).lower()

        for item in diff_list:
            if response == item[0] or response == item:
                return item

        print("!!! Please choose a valid difficulty !!!")
        print()


diff_list = ["easy", "moderate", "hard"]

ask_diff = difficult("What difficulty would you like? ")

# Selects mode based on response
if ask_diff == "easy":
    mode = "easy"

elif ask_diff == "moderate":
    mode = "moderate"

else:
    mode = "hard"

if mode == "easy":
    a_side = random.randint(1, 10)
    o_side = random.randint(1, 10)
    h_side = math.sqrt(a_side ** 2 + o_side ** 2)

if mode == "moderate" or mode == "hard":
    a_side = random.randint(10, 20)
    o_side = random.randint(10, 20)
    h_side = math.sqrt(a_side ** 2 + o_side ** 2)

print("Mode Selected: ", mode)
print("Adjacent side: ", a_side)
print("Opposite side: ", o_side)
print("Hypotenuse: ", round(h_side))
