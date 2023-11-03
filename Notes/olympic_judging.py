# Question 2: Olympic Judging
# Author: Jason C
# Date: Nov 3

total_score = 0

for i in range(1, 6):
    judge_score = float(input(f"Judge {i}:"))
    total_score += judge_score

average_score = total_score / 5

print('Your Olympic score is',round(average_score, 1))