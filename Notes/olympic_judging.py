# Question 2: Olympic Judging
# Author: Jason C
# Date: Nov 3

judge_number = 1
NUMS_RESPONDENTS = 5
sum = 0.0

for i in range(NUMS_RESPONDENTS):
    judge = float(input("Judge " + str(judge_number) + ": "))
    sum += judge
    judge_number += 1

average_score = sum / NUMS_RESPONDENTS

print("Your Olympic score is:", average_score)