# Yes / no / why response function
def user_input(question, valid_list, error):
    while True:
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


yesno_list = ["yes", "no", "why", "xxx"]
diff_list = ["easy", "medium", "hard", "xxx"]

# Testing purposes...
yesno = user_input("Choose Yes / No / Why: ",
                   yesno_list,
                   "Please enter a valid response (y / n / w)")

print()

diff = user_input("Input a difficulty: ",
                  diff_list,
                  "Please enter a valid difficulty (e / m / h)")

print()

print(f"Response: {yesno}\nDifficulty: {diff}")
