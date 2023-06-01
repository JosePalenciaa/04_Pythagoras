def difficult(question):
    while True:
        response = input(question).lower()

        for item in diff_list:
            if response == item[0] or response == item:
                return item

        print("Please choose a valid difficulty ")
        print()


diff_list = ["easy", "moderate", "hard", "xxx"]

ask_diff = difficult("What difficulty would you like? ")

if ask_diff == "easy":
    difficulty = "easy"

elif ask_diff == "moderate":
    difficulty = "moderate"

elif ask_diff == "hard":
    difficulty = "hard"


