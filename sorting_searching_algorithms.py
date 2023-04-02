


# Insertion sort
def insertion(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

list = [5, 4, 3, 2, 1]
insertion(list)
print(list)


list = [5, 6, 7, 10, 5, 4, 2]

# linear search
def linear_search(list, target):
    for idx, value in enumerate(list):
        if (target == value):
            return f'Target: {target} is located at index: {idx}.'
    return f'{target} is not in the list.'

linear_result = linear_search(list, 1)
print(linear_result)
print()

# Binary search
# divide the list in half, if target is greater than value at middle,
# divide another half of the list
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last: # each loop causes the data set to decrease by half: O(ln n)
        midpoint = (first + last) // 2 # floor division, rounds down to nearest whole number
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

list.sort()
binary_result = binary_search(list, 2)
print(f'Binary Search: list: {list} {binary_result}')

# recursive binary
def rec_binary(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return rec_binary(list[midpoint + 1:], target)
            else:
                return rec_binary(list[:list[midpoint]], target)

print(len(list) - 1)
print()


# Rotated lists
# Given a rotated sorted list that was rotated an unknown number of times, find the number of times it was rotated
# Find the midpoint in the list with binary search
# Find the count of numbers in the list before the smallest number
def rotated_list(rotated):
    count = 0
    first = rotated[0]
    last = len(rotated) - 1
    mid = (first + last) // 2



def my_binary_search(list, value):
    first = list[0]
    last = len(list) - 1

    while first < last:
        mid = (first + last) // 2
        if mid == value:
            return mid
        if value < mid:
            last = mid - 1
        elif value > mid:
            first = mid + 1
    return None

print(f'My Binary: {list} {my_binary_search(list, 2)}')
