import random

random_integer = random.randint(10,100)
print (random_integer)

#random.random do float number between 0.0 to 1.0 -> 0.0000000... - 0.99999999...
random_float = random.random() * 100
print (random_float)

love_score=random.randint(1,100)
print (f"Your love score is {love_score}")