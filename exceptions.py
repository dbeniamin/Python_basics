try:
    Age = int(input("Age:"))
    income = 20000
    risk = income / Age
    print(Age)  # calculating various values based on age input
except ZeroDivisionError:
    print("Age cannot be 0!")
except ValueError:
    print("Invalid Value")
# if the user enters an invalid value, line 2 error
# except is used to catch the error types ( value error, zero division)
# try and except blocks are used to handle exceptions that are raised in our programs
