current_courses = input("How many courses are you taking? ")
NUMS_RESPONDENDTS = current_courses
course_num = 1
sum = 0
for _ in range(int(NUMS_RESPONDENDTS)):
    course_evaluation = input("How do you rate course " + str(course_num) + " out of 5? ")
    course_num += 1
    sum += int(course_evaluation)
course_average = sum / int(NUMS_RESPONDENDTS)
if course_average <= 1:
    print("Ouch!")
elif course_average > 1 and course_average < 3:
    print("Not a bad semester.")
else:
    print("Glad to hear that!")
