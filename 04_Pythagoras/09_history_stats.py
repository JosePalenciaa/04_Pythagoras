game_summary = []
rounds_played = 5
rounds_lost = 0
rounds_won = 0

# testing purposes...
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

print()
print("*** Game History ***")
for game in game_summary:
    print(game)