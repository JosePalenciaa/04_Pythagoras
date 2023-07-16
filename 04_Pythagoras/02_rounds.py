def int_checker(question):

    while True:
        response = input(question)

        error = "Please enter a valid integer greater than 0"

        if response == "xxx":
            return response

        elif response != "":
            try:
                response = int(response)

                if response < 1:
                    print(error)
                    continue

            except ValueError:
                print(error)
                continue

        return response


# Rounds mechanics
rounds_played = 0
rounds_won = 0
rounds_lost = 0

rounds = int_checker("How many rounds (<ENTER> for infinite): ")

# rounds loop
end_game = "no"
while rounds != "xxx":

    if rounds == "":
        print()
        heading = f"Round {rounds_played + 1} of Continuous Mode"

    else:
        print()
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)
    choose = input(f"Enter a number or 'xxx' to end: ")
    rounds_played += 1

    if rounds_played == rounds:
        break

    elif choose == "xxx":
        break

print("Thank you for playing")
