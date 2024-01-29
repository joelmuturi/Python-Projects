#welcome to the tip calculator!
print("Welcome to the tip calculator!")
#what was the total bill?
bill = float(input("what was the total bill? $ "))
#what percentage tip would you like to give? 10, 12, or 15?
tip = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
#How many people to split the bill?
people = int(input("how many people to split the bill? "))
#Each person should pay:
#bill_with_tip = tip / 100 * bill + bill
#print(bill_with_tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
print(bill_per_person) 
