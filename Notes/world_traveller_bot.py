user_name = input("What's your name?\n")
print(f"Nice to meet you, {user_name}!")

continents = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antarctica"]
visited_continents = 0
total_continents = 7

for continent in continents:
    response = input(f"Have you been to {continent}? (yes/no)").lower()
    

    if response == 'yes':
        visited_continents += 1
    elif response != 'no':
        print("Please enter 'yes' or 'no' as a response.")

print(f"I see, you've visited {visited_continents}/{total_continents} continents!")





