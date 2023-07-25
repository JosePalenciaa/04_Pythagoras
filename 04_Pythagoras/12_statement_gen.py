# Copied from Lucky Unicorn
def statement_generator(statement, decoration, above_below, has_emoji=None):
    sides = decoration * 3

    # statement = "{} {} {}".format(sides, statement, sides)
    statement = f"{sides} {statement} {sides}"

    if has_emoji == "yes":
        top_bottom_length = len(statement) + (len(sides) * 2) + 2
    else:
        top_bottom_length = len(statement)

    top_bottom = above_below * top_bottom_length

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Trialing
statement_generator("Womp Womp", "👌", "=", "yes")
