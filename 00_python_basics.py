# Python from NON Programmers

# Variables -- holds modifiable data

wallet_int = 10  # example of integer available
wallet_float = 9.9  # example of float variable
wallet_str = "test"  # example of string variable
wallet_boolean = True  # example of boolean variable ( booleans can only be True or False)

# Access the value or status of a variable by using print statement
print(wallet_float)

day_1 = 8

# Ints ( integer ) and Floats -- holds modifiable number values

temp_1 = -15  # ints and floats cand have negative numbers
height = 180.5  # example of float

print(height / temp_1)  # arithmetic operations can be done using ints and floats

# Strings -- refers to words and sentences, requires the usage of " " or ' '

shirt = "blue"
print(shirt)

# use \' or \" to tell the program not to treat the marks as string ender.

store = 'this is a really "nice" string to test\'s'
movie = "Shawshank Redemption"

# Variables in Strings

day = 21
month = "October"
temp = 65

print(f"Today is {day} of {month} and there are {temp} degrees")

# Boolean  -- represents the state of True or False

light_is_on = True

if light_is_on:
    print("The light is on")

# Comparison and Else

light_is_on = False

if light_is_on:
    print("The light is on")
else:
    print("no light")

weight = 115

if weight < 119:
    print("you are good")
else:
    print("kinda heavy :d")

age_target = 38

if age_target < 18:
    print("You are a child")
else:
    print("You are an adult")


# ODD / EVEN exercise
# number var
# return True if odd and return False if even

def your_code():
    number = 7
    if number % 2 == 0:
        return False
    else:
        return True


your_code()
