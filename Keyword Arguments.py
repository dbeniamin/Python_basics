def greet_user(first_name, last_name):
    print(f" Hy {first_name} {last_name} !")
    print(" Welcome aboard")


print("Start")
# keyword argument is always after positional argument
greet_user(last_name="Drimus", first_name="Beni")
print("Finish")
