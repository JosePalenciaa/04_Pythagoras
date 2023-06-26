def instructions():
    print("---------------------")
    print("**** How to Play ****")
    print("---------------------")
    print()
    print("Your goal is to calculate the missing side using the 'Pythagoras Theorem'..."
          "\n• Formulas:\n\tHypotenuse | a² + b² = c²\n\tOpposite | c² - a² = b²\n\tAdjacent | c² - b² = a²"
          "\n\tHypotenuse = c | Opposite / Adjacent = b / a"
          "\n\n• First select a difficulty."
          "\n• You are given 3 attempts. "
          "\n• Solve the missing side. "
          "\n• Round your answer to a whole number / integer."
          "\n• Can you win?")
    print()


def yes_no_why(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no / why)")
        print()


yesno_list = ["yes", "no", "why"]

# Loop for testing purposes...
while True:
    display_instructions = yes_no_why("Do you want to see Instructions? ")

    if display_instructions == "yes":
        instructions()

    elif display_instructions == "why":
        print("Because I said so!!!")

    # Used for test cases checker
    elif display_instructions == "no":
        print("Program Continues")
