# Tip Calculator
print("Welcome to the Tip Calculator App!")

# prompt for the total bill, convert input to float type
total_bill = float(input("\nWhat is your total bill? $"))
# prompt for the tip percent, convert to interger
tip_percent = int(input("\nWhat percentage tip would like to give? 10, 12 or 15? "))
# prompt for number of guest, convert to integer
total_guest = int(input("\nHow many people to split the bill? "))

# bill for each guest
bill_for_each = round((total_bill / total_guest) * (1 + (tip_percent / 100)), 2)

print(f"\nEach person should pay {bill_for_each}")
