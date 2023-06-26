import random
import math
a_side = random.randint(10, 20)
o_side = random.randint(10, 20)
h_side = math.sqrt(a_side ** 2 + o_side ** 2)

print("Adjacent side: ", a_side)
print("Opposite side: ", o_side)
print("Hypotenuse: ", h_side)
