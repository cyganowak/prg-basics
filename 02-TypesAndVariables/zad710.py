import random
computer = random.randint(1, 6)
user = int(input("Guess the number (between 1 and 6): "))
print(f"Did user guess correctly? {user == computer}")