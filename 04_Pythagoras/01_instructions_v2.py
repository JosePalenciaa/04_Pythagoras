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
# Looping to so user response of 'why' outputs statement, and reruns the question
while True:

    display_instructions = yes_no_why("Would you like to see Instructions? ")
    # Gets angry at user if they respond with 'why', loop continues until user answers 'yes' or 'no'
    if display_instructions == "why":
        print("Because I said so!!!")
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

print("program continues")
