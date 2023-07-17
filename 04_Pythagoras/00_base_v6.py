# Yes / no / why response function
def user_input(question, error):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        for item in diff_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


yesno_list = ["yes", "no", "why", "xxx"]
diff_list = ["easy", "medium", "hard", "xxx"]

# Testing purposes...
yesno = user_input("Input anything: ", "Please enter a valid response (y / n / w)")
print(yesno)

diff = user_input("Input a difficulty: ", "Please enter a valid difficulty (e / m / h)")
print(diff)

print()
print(f"Response: {yesno}\nDifficulty: {diff}")
