game_summary = []
rounds_played = 5
rounds_lost = 0
rounds_won = 0

# testing purposes...
for item in range(1, 6):
    result = input("Choose result: ")

    outcome = f"Round {item}: {result}"

    if result == "lose" or result == "l":
        rounds_lost += 1

    elif result == "win" or result == "w":
        rounds_won += 1

    elif result == "xxx":
        break

    game_summary.append(outcome)

# Calculate game stats
percent_win = round(rounds_won / rounds_played * 100, 1)
percent_lose = round(rounds_lost / rounds_played * 100, 1)
percent_not_played = round(100 - percent_lose - percent_win, 1)

print()

# displays game stats with %
# values to nearest who number
print("*** Game Statistics ***")
# Percentages - win / lose / not played
print(f"You won: {percent_win}%")
print(f"You lost: {percent_lose}%")
print(f"You didn't play: {percent_not_played}%")

# Thanks the user for playing the quiz
print("\nThanks for playing!")
