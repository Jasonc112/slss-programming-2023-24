questions = ["Did you eat?", "Did you study?", "Did you do your laundry?", "Did you call grandma?"]
count = 0

for questions in questions:
    if input(questions) == "yes":
        count += 1

if count == 0: 
    print("I'm coming over")

elif count >= 1 and count <= 2:
    print("Ok")

else:
    print("Good!")


