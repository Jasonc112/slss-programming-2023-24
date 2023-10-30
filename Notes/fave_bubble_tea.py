# Bubble Tea Popularity Algorithm
# Author: Jason
# Date: 26 October 2023

# Ask 5 users what their favourite bubble tea palce is
# Prints out a summary of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 5

# ------

# Like counters
coco_likes = 0       # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask 5 users what their favourite bubble tea palce is
    # Store that information somewhere
    print("What's your favourite bubble tea place?")

    fave_place = input().strip(",.?! ").lower()

    # Tally or counting algo
    # Options: CoCo, Suntea, Chatime, Bubble Queen
    # If they choose any of these options, increase the counter 
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1       # alternate to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1

# Repeat the code above 5 times

# Print out a summary of all the places
# Give the raw score AND the score as percentage
total = coco_likes + chatime_likes + suntea_likes + bubqueen_likes
print(f"CoCo Likes: {coco_likes}")
print("The percentage is: " + str(coco_likes / total * 100) + "%" )
print(f"Chatime Likes: {chatime_likes}")
print("The percentage is: " + str(chatime_likes / total * 100) + "%" )
print(f"Suntea Likes: {suntea_likes}") 
print("The percentage is: " + str(suntea_likes / total * 100) + "%" )
print(f"Bubble Queen Likes: {bubqueen_likes}")
print("The percentage is: " + str(bubqueen_likes / total * 100) + "%")