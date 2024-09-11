import random
import time

print("Please guess a number between 1 and 10 !")
time.sleep(2)
print("Picking a number .... ")
time.sleep(2)
guess = int(input("What is the number?: "))
guess_count = 1

correct_number = random.randint(1, 10)

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        time.sleep(1)
        guess = int(input(" Too LOW \n What is the number?: "))
    else:
        time.sleep(1)
        guess = int(input("Too High \n What is the number?: "))

print(f"Right Answer was {guess}, It took you {guess_count} guesses")
