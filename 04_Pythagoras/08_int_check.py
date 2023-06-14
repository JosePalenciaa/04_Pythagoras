def int_check(question, low=None, high=100, exit_code=None):

    if low is None and high is None:
        error = "Please enter a valid integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (i.e., not too low / too high, etc.)
            if situation == "any integer":
                return response

            elif situation == "both" and low <= response <= high:
                return response

            elif situation == "low only" and response >= low:
                return response

            print(error)

        except ValueError:
            print()
            print(error)
            continue

