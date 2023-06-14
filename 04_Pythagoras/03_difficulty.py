def difficult(question):
    while True:
        response = input(question).lower()

        for item in diff_list:
            if response == item[0] or response == item:
                return item

        print("!!! Please choose a valid difficulty !!!")
        print()


diff_list = ["easy", "moderate", "hard", "xxx"]

# loop for testing purposes...
while True:
    ask_diff = difficult("What difficulty would you like? ")

    print(ask_diff)
    print()
