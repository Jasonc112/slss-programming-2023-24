# Star Wars Bot
# Author: Jason
# Date: Oct 16 2023

# Ask the user if they like red or capes
print("I will decide if you can join the dark side.")
like_red = input("Is red your favourite color? ")
like_capes = input("Do you like capes? ")

# Give response based on inputs
if like_red.lower() == "yes":
    print("Dark side it is!")
elif like_red.lower() == "no":
    if like_capes.lower() == "yes":
        print("The dark side is your chosen path.")
    else:
        print("I don't think the dark side is your path.")
        print("Please choose carefully")
else:
    print("You are not allowed to join the dark side")
    print("Go join the light side.")