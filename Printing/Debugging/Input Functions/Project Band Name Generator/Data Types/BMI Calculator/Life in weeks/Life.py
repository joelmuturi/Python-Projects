#create a program using maths & f-strings that tells us how many days, weeks, months, we have left if we live until 90yrs old
#it will take your current age as the input & output a message with our time left in this format:
#You have x days, y weeks and z months left; where x, y, & z are replaced with the actual calculated numbers.
age = int(input("enter your current age: "))
years_rem = 90 - age
days_rem = years_rem * 365
weeks_rem = years_rem * 52
months_rem = years_rem * 12
#f-string
message = f"You have {days_rem} days, {weeks_rem} weeks and {months_rem} months left" 
print(message)
