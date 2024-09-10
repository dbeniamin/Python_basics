# def keyword used to defin a function

def function_testing(name):
    print(f"Test print function {name}")


# calling the function is required to execute the existing code
function_testing("Benjamin$$")


# looping over a range and use the function_testing() call to to the code for range ammount of times
# for x in range(50):
#     function_testing()

# parameters - a way to pass information in to the function

def add_numbers(num1, num2):
    print(num1 + num2)


add_numbers(1234, 555)


# Challange dog func that takes age and name and prints the complete data

def dog_data(name, age):
    print(f"The dog's name is {name} and he is {age} old")


dog_data("Random Dog", 11)


# returning the func values

def multiplications(num):
    return num * 11


test_num = multiplications(55)
print(test_num)


# Challange - create a func that returns a string in all caps

def upper_case(var):
    return var.upper()


upper_case("test string this")

names = ["ben", "Jhon", "arthur"]
for name in names:
    print(upper_case(name))

# comments are a very import thing in to code blocks to hold main ideas or processe
# # -> used to coment a line that will be in the file but not executed


# Inputs -> requesting the user for an input

# asking the user to input some text
user_text = input("enter some text: ")

print(user_text.upper())
# Input from the console is always a string !!!
user_selection = input("do you want it uppercased? y / n: ")
if user_selection == "y":
    print(user_text.upper())
else:
    print(user_text.lower())


# Coding Challange - Is there a remainder?
# num1 = 1122334455
# num2 = 55
# num1 and num2 - passed when calling function

def has_remainder(num1, num2):
    if num1 % num2 == 0:
        return False
    else:
        return True


has_remainder(1122334455, 55)
