# Simple program to remove duplicates from a list
my_list = [1, 2, 6, 3, 4, 2, 4, 5, 5, 12, 5, 1]

unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
        my_list = unique_list
        
print(my_list)