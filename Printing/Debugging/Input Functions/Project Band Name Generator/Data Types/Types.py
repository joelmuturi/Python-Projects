#write a program that adds the digits in a 2 digit number eg if the input was 35, the output should be 3+5=8
two_digit_number = input("Enter a two digit number:")
#check the data type of the two_digit_number 
print(type(two_digit_number))
#get the first & second digits using subscripting, then convert string to int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
#add the two digits together
two_digit_number = first_digit + second_digit
print(two_digit_number)