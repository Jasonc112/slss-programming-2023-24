# Question 3: Mcdonald
# Author: Jason
# Nov 3

# Define the prices
burger_price = 5
fries_price = 3
tax_rate = 0.14


burger_choice = input("Would you like a burger for $5? (Yes/No) ").strip(",.?! ").lower()

total_cost = 0

if burger_choice == "yes":
    total_cost += burger_price

fries_choice = input("Would you like fries for $3? ").strip(",.?! ").lower()

if fries_choice == "yes":
    total_cost += fries_price

total_with_tax = total_cost + (total_cost * tax_rate)

print(f'Your total is ${total_with_tax:.2f}')