# Yes / no / why response function
def user_input(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        for item in diff_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response")
        print()


yesno_list = ["yes", "no", "why", "xxx"]
diff_list = ["easy", "medium", "hard", "xxx"]

# Testing purposes...
while True:
    testing = user_input("Input anything: ")

    print(testing)
