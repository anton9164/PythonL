number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
number3 = int(input("Enter the third number:"))
largest_number = number1
if largest_number < number2:
    largest_number = number2
if largest_number < number3:
    largest_number = number3
print("The largest number is:", largest_number)
# This program takes 3 int inputs from user and check whci hnumber is the largest from these 3 numbers and print the largest number in the end.
