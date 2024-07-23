generic_list = [1, 3, 5, 7, True, "test", "string"]  # any variable type can be stored in a list

fav_movies = ["Dune", "Shawshank Redemption", "Lost"]

# prints the 1st item in the list, list items can be accessed by taping in the index starting from 0
print(fav_movies[0])

print(len(fav_movies))  # len finds the length of a list - ie the number of items that are on the list.

# adds an item at the end of a list
fav_movies.append("Batman")

# inserts an item at the given index
fav_movies.insert(2, "Test movie")

# deletes the item at the given index in the list
del (fav_movies[1])

# For Loops
# go through a range and do some actions
for number in range(10):
    print("Test")

# the naming of the var while looping through a range can be done freely

fav_movies = ["Dune", "Shawshank Redemption", "Lost"]

for movie in fav_movies:
    print(movie)

for n in range(40):
    if n % 2 == 0:
        print(n)

# Dictionaries
# The pairing of keys and values

cars = {"Bmw": 2000, "Jaguar": 1900, "Range Rover": 1985}

# values can be printed by providing the key
print(cars["Jaguar"])

# adding key and value pairs to a dictionary
cars["Audi"] = 2002

# deleting a key and value pair from a dictionary by providing the key
del (cars["Bmw"])

# create a dict with ints for keys and Booleans for values
test_dict = {
    1: True,
    2: False,
    3: False,
    4: True
}


# Code Exercise -  Sum of all evens

# Approach 1
def your_code():
    numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return sum(evens)


# Approach 2
def your_code_2():
    numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
    total = 0
    for number in numbers:
        remainder = number % 2

        if remainder == 0:
            total = total + number

    return total
