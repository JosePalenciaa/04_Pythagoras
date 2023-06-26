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
    mode = "easy"

elif ask_diff == "moderate":
    mode = "moderate"

elif ask_diff == "hard":
    mode = "hard"

print(f"You've selected the {ask_diff} difficulty")
