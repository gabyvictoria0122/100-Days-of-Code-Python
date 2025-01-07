print("Welcome to the tip calculator!")
bill = float(input("What as the total bill? $"))
percentage = float(input("What percentage tip would you like to give? "))
tip_value = bill * (percentage/100)
total_amount = bill + tip_value
print(f"The tip value is: ${tip_value}")
print(f"The total amount to be paid is: ${total_amount}")
