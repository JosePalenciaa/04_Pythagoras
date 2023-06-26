import math
import random

# Trialing...
side_a = random.randint(1, 10)
side_b = random.randint(1, 10)

# Outputs...
side_c = math.sqrt(side_a ** 2 + side_b ** 2)

print("The Adjacent is:", side_a)
print("The Opposite is:", side_b)
print("It is...", round(side_c))
