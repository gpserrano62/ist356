
# Let’ write a program to divide up the check among diners in a party.

# Write a program to input the amount of a restaurant check, tip %, and number of diners

# The program should output the total amount with tip, and the amount each diner owes.

check_amount = float(input("Enter the amount of the restaurant check: $"))
tip_percent = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
num_diners = int(input("Enter the number of diners: "))

if check_amount < 0 or tip_percent < 0 or num_diners < 0:
	print("Error: values cannot be negative.")
	exit()

tip_amount = check_amount * (tip_percent / 100)
total_amount = check_amount + tip_amount
amount_per_diner = total_amount / num_diners

print(f"Total amount with tip: ${total_amount:.2f}")
print(f"Amount each diner owes: ${amount_per_diner:.2f}")

