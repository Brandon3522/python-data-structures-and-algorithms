import random as random


# Fizzbuzz

def fizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'


list = [3, 5, 15, 20, 25, 30, 9, 3]
for value in range(len(list)):
    print(f'Value {value}: {fizzBuzz(value)}')


# Reverse string
def reverse(string):
    return string[::-1]

print(reverse('love'))

# Remove duplicates
def remove_duplicates(list):
    conversion = set(list)
    return conversion

print(remove_duplicates(list))

# Number guessing game
def guess_number():
    randomNum = random.randint(0, 100)

    userNum = int(input('Guess the number from 0 to 100: '))

    while userNum != randomNum:
        if userNum < randomNum:
            print(f'The number is greater than {userNum}.')
        elif userNum > randomNum:
            print(f'The number is less than {userNum}.')
        elif userNum == randomNum:
            print(f'Congrats! {randomNum} is the correct guess.')
            break
        userNum = int(input('Guess the number from 0 to 100: '))

# guess_number()
print()

# Determine sum of s continuous elements in array. Return -1 if s is not valid
# Iterate through the list
# If s is greater than length, return -1
# Add values up to s
def sum_continous(list, s):
    sum = 0
    if s > len(list):
        return -1
    else:
        for index, value in enumerate(list):
            if (s <= 0):
                return sum
            sum += list[s - 1]
            s -= 1
        return sum

sum_list = [5, 3, 1, 2]
print(sum_continous(sum_list, 2))
print()

# Sliding window
# Given an array of ints and 2 integers k and threshold, return the number of sub-arrays of size k
# and average greater than or equal to threshold
# def my_sliding_window(array, k, threshold):
#     counter = 0
#     sum = 0
#     window = array[:array[k]]
#     for i in range(len(array)):
#         sum += array[i]
#         if i > k:
#             break
#
#     window = array[k + 1, array[k]]
#     if sum >= threshold:
#         counter += 1
#     for i in range()


# Sliding window
# Given an array of ints and 2 integers k and threshold, return the number of sub-arrays of size k
# and average greater than or equal to threshold
def sliding_window(array, k, threshold):
    count = 0
    sum = 0
    # Find sum of first k units
    for i in range(len(array)):
        sum += array[i]
        if i >= k:
            break
    average = int(sum / k)
    if average >= threshold:
        count += 1 # update count
    j = k
    # rest of array
    while j < len(array):
        # slide window up one element
        sum -= array[j - k]
        sum += array[j]
        # calculate the average of these k elements
        currAverage = int(sum / k)
        # update counter
        if currAverage >= threshold:
            count += 1
        j += 1
    return count

arr = [2, 2, 2, 2, 5, 5, 5, 8]
slide_result = sliding_window(arr, 3, 4)
print(slide_result)

print('#########################')
# Palindrome
# Given a string, determine if it's the same forward and backward
# Return true or false boolean
def is_palindrome(string):
    # determine reverse of string
    reverse = string[::-1]

    # if strings match return true, otherwise false
    if (string == None or string == ''):
        return False
    elif (reverse == string):
        return True
    else:
        return False

palindrone_test = 'malayalam'
palindrone_result = is_palindrome(palindrone_test)
print(f'Palindrone: {palindrone_test} - {is_palindrome(palindrone_test)}')
print()

def longest_of_2(word, word2):
    longest = 'Neither'
    if len(word) <= 0 or len(word2) <= 0:
        return longest
    if len(word) > len(word2):
        longest = word
    elif len(word) == len(word2):
        longest = 'equal'
    else:
        longest = word2
    return longest

longest_of_2_result = longest_of_2('', '')
print(longest_of_2_result)
print('#########################')

def insertion_sort(list: list):
    for n in range(1, len(list)):
        curr = list[n]
        j = n
        while j > 0 and list[j-1] > curr:
            list[j] = list[j-1]
            j -=1
        list[j] = curr
    return list
sorted_list = insertion_sort([5,3,2,1])
print(f'Insertion: {sorted_list}')
print('#########################')

def min_val(list: list):
    min = list[0]
    for n in range(1, len(list)):
        if list[n] < min:
            min = list[n]
    return min
min_value = min_val([1, 0, -1, 2, 5])
print(f'Min: {min_value}')
print('#########################')

# Return index of value in list
def find_index(list: list, val: int):
    index = 0
    for n in range(len(list)):
        if list[n] == val:
            index = n
            return index
index = find_index([0,5,1,2,3,10], 10)
print(f'Index: {index}')
print('#########################')

def capsEveryOtherLetter(str: str):
    result = ''
    if len(str) == 0:
        return result
    else:
        for i in range(len(str)):
            if i == 0:
                result += str[i].upper()
            elif i % 2 == 0 and i > 0:
                result += str[i].upper()
            else:
                result += str[i]
        # result = ''.join(result)
        return result

caps_every_other = capsEveryOtherLetter('hello')
print(f'Caps every other letter: {caps_every_other}')
print('#########################')

# Fizzbuzz with dictionary
rules = {
    3: 'Fizz',
    5: 'Buzz'
}
# Print from 1 to n
def better_fizzBuzz(n: int):

    for num in range(1, n + 1):
        result = ''
        for key, val in rules.items():
            if num % key == 0:
                result += val
        if result:
            print(f'{num}: {result}')
        else:
            print(f'{num}: None')


better_fizzBuzz(15)















