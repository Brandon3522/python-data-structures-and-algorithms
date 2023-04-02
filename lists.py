

##############################
# Lists
# List functions: len, max, min, sum
# -1 index accesses end of list
# Range: from zero to 1 less than parameter, goes through positions

names = ["John", "Bob", "Pop", "Sarah"]
print(names)
print(names[0])

# Prints a range from index's specified

print(names[2:])
# Find largest number algorithm

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = numbers[0]
for item in numbers:
    if item > largest:
        largest = item
print(f"The largest number is {largest}")

#########################################
#



#########################################
# 2D lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

# Print all numbers in matrix
for row in matrix:
    for item in row:
        print(item)

######################################
# List methods
# append, count, extend, index, insert, pop, remove, reverse, sort
numbers = [5, 2, 1, 7, 4]
numbers.append(13)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
print(numbers.index(4))

# Check for existence of 50 in list
print(50 in numbers)

# Sort the list
numbers.sort()
print(numbers)

# Copy list
numbers2 = numbers.copy()
numbers2.append(124)
print(numbers2)
print("")

# Program to remove duplicates
# Create empty list
# Take each number in list and look for duplicate
# If duplicate is not found in new list, add to new list
list_num = [1, 1, 2, 2, 3, 4, 5, 6, 8, 10]
unique_list = []
for item in list_num:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
