# This program creates a list of numbers, and it allows the user to replace middle number
# After replacing the middle number, program deletest the last number and prints the length of the list
hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Replace the middle number in the list: "))
del hat_list[4]
print("The length of the list is:", len(hat_list))
print("The list is: ",hat_list)
hat_list.insert(2,15)
hat_list.append(20)
print(hat_list)