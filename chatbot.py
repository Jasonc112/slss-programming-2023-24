# Chatbox
# Author: Jason
# Date: 20 September 2023

import random
import time

# Greet the user
print("Hello there! 🤖")

# Pause for 1.5 seconds
time.sleep(1.5)
print("I'm a crude Chatbox, here to talk to you.")
time.sleep(1.5)

# Get the user's name and store it in a variable
user_name = input("So... What's your name? ")

# Respond with the user's name in a friendly way
time.sleep(1.5)
print(f"It's good to meet you, {user_name}.")

# Ask the user what their favourite food is
time.sleep(1)
favourite_food = input("What's your favourite food? ")

# Make a comment about their food
# Create a list of possible responses
list_of_food_responses = [
    f"Oh. I've never had {favourite_food} before.",
    "Mmmmmmmm. That sounds good!",
    "I heard that that is delicious.",
    "Cool."
]

time.sleep(1.5)

# Choose one of those responses randomly

random_food_response = random.choice(list_of_food_responses)

# Print out that chosen response 
print(random_food_response)