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

mode = ""

if ask_diff == "easy":
    mode = "easy"

elif ask_diff == "moderate":
    mode = "moderate"

elif ask_diff == "hard":
    mode = "hard"

print(ask_diff)
