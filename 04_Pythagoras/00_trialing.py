def difficult(question):
    while True:
        response = input(question).lower()

        for item in diff_list:
            if response == item[0] or response == item:
                return item

        if question == "easy":
            print("Easy Mode")

        elif question == "moderate":
            print("Moderate Mode")

        elif question == "hard":
            print("Hard Mode")

        elif question == "xxx":
            break

        print("Please enter a valid response (yes / no / why)")
        print()


diff_list = ["easy", "moderate", "hard", "xxx"]

ask_diff = difficult("What difficulty would you like? ")

