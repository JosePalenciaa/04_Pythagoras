game_summary = []
rounds_played = 5
rounds_lost = 0
rounds_won = 0

for item in range(0, 5):
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
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print("*** Game History ***")
for game in game_summary:
    print(game)

print()

# displays game stats with %
# values to nearest who number
print("*** Game Statistics ***")
print(f"You won {percent_win}% and lost {percent_lose}% of the rounds.")
