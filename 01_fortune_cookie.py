import random

response = random.randint(1,100)

fortune_number = random.randint(1,3)
fortune_text = ""

if fortune_number == 1:
    fortune_text = "You will have a great day"
if fortune_number == 2:
    fortune_text = "You will have a number 2 day"
if fortune_number == 3:
    fortune_text = "You will have a below average day"


print(f"{fortune_text} The lucky number is {response}")