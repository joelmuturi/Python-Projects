#write a program that interprets the BMI based on a user's weight and height.
#it should tell them the interpratation of their BMI based on the BMI value
#under 18.5 they are underweight
#over 18.5 but below 25 they have a normal weight
#over 25 but below 30 they are overweight
#over 30 but below 35 they are obese
#above 35 they are clinically obese
#warning: you should round the reslt to the nearest whole number
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
#BMI = round(weight / height **2)
BMI = float(input("enter BMI value: "))
if BMI < 18.5:
    print("they are underweight")
elif BMI < 25:
    print("they have a normal weight")
elif BMI < 30:
    print("they are overweight")
elif BMI < 35:
    print("they are obese")
else:
    print("they are clinically obese")