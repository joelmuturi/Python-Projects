#write a program that calculates the body mass index(BMI) from user's weight and height
height = input("enter height in m :")
weight = input("enter weight in kg :")
BMI = int(weight) / float(height) **2
BMI_as_int = int(BMI)
print(BMI_as_int)
 