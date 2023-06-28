for item in range(0, 10):
    is_even = item % 2
    print(f"{item} % 2 = {is_even}")

    if is_even == 0:
        print("is even")
    else:
        print("is odd")