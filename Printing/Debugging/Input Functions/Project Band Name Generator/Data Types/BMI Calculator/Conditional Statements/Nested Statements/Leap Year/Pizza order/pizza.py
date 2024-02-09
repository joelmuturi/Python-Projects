#congratulations, you've got a job at Python pizza.
#your first job is to build an automatic pizza order program. Based on user's order, work out their final bill.
#small pizza: $15
#medium pizza: $20
#large pizza: $25
#peperroni for small pizza: + $2
#peperroni for medium or large pizza: + $3
#extra cheese for any size pizza: + $1
print("welcome ptyhon pizza deliveries!")
size = input("what size of pizza do you want? S, M or L ")
add_peperroni = input("should we add peperroni? Y or N ")
extra_cheese = input("do you want extra cheese? Y or N ")
bill = 0
if size == 'S':
    bill +=15
elif size == 'M':
    bill +=20
else:
    bill +=25
if add_peperroni == 'Y':
    if size == 'S':
        bill +=2
    else:
        bill +=3
if extra_cheese == 'Y':
    bill +=1
    print(f"your total bill is ${bill}")


