import random

x = random.randint(3, 10)
odd_even = x % 2

if odd_even == 0:
    print("is even")

    a = x
    b = (x/2)**2 - 1
    c = (x/2)**2 + 1

else:
    print("is odd")

    a = x
    b = (x**2 / 2) - 0.5
    c = (x**2 / 2) + 0.5

print(f"\na = {a}, b = {b}, c {c}")
