import math

# Function
def test_function():
    print("Test Function call")
    print("")
    return


print("Hello World!")
print("")

str1 = "Hello World!"

print(str1)
print(str1[0])

counter = 1

# List
print(counter)
print("")
print(str1 + " " + "Counter")
print("")
listOf = ["List1", "List2", "List3", "List4"]

print(listOf[1])

# True and False case sensitive
# if else statements
var1 = 260
var2 = 200
print("")
if var1 < 200:
    print("Variable less than 100")
elif var1 > 250:
    print("Greater than 250")

test_function()

print("#########################")

def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

print(gcd(16, 4))

print('')
###############################################
# User input
'''
name = input('What is your name? ')
fav_color = input('What is your fav color? ')
print('Hello ' + name + ' your fav color is ' + fav_color)
'''
##############################################
# type conversion
'''
# input function returns a string var
birth_year = input('Birth year: ')
age = 2021 - int(birth_year)
print(age)
weight = input("Enter your weight in pounds: ")
weight_kilograms = int(weight) * 0.45
print(weight_kilograms)
'''
####################################
# strings
'''
# ''' ''' for multiline strings
course = "Python"
print(course[0])
# Print from index 0 to 4
print(course[0:4])
# formatted strings
first = "John"
last = "Smith"
message = f'{first} [{last}] is a coder'
print(message)
'''
##################################
# String methods
#
'''
course = 'Python'
print(len(course))
print(course.upper())
print(course.find('P'))
# Returns boolean for string in variable
print('Python' in course)

# .join method
string_list = ['a'] * 4
# wrong, generates a new string on each loop
new_string = ''
for i in string_list:
    new_string += i
# better way with join method
string_list = ''.join(new_string)
print(new_string)

'''
######################################
# Math functions
'''
# Import Math for advanced functions
print(math.ceil(2.9))
print(math.floor(2.9))
x = 2.9
print(round(x))
print(abs(-2.9))
'''
#########################################
# IF, ELSE statements
'''
house_price = 1000000
credit = False
if credit:
    downPay = house_price * .1
else:
    downPay = house_price * .2
print(f'Down payment: ${downPay}')
'''
#######################################
# Logical and comparison operations
'''
# and not = && !
has_high_income = True
has_good_credit = True
if has_good_credit and has_high_income:
    print("Eligible for loan")
if has_good_credit or has_high_income:
    print("Good to go")
temp = 50
if temp > 30:
    print("Its hot as fuck")
elif temp < 10:
    print("Its cold as tits")
else:
    print("It's a lovely day")
'''
#################################
# Weight converter
'''
# get weight, ask for lbs or kgs, convert to opposite of selected
weight = int(input("Weight: "))
weight_type = input("(L)bs or (K)g: ")
# weight_type.upper() == "L" will also work
if weight_type == "l" or weight_type == "L":
    weight *= .45
    print(f"You are {weight} kilos")
elif weight_type == "k" or weight_type == "K":
    weight /= .45
    print(f"You are {weight} pounds")
else:
    print("Error!!!")
'''
##################################
# Loops
'''
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")
'''
###################################
# Guessing game
'''
secret_num = 9
counter1 = 0
guess_limit = 3
while counter1 < guess_limit:
    guess = int(input("Guess: "))
    counter1 += 1
    if guess == secret_num:
        print("You win")
        break
else:
    print("You done fucked it up")
'''
#####################################
# Car game
'''
# if user types help display options, if user types start, print the car is started
# if the user types stop, print stop the car, if the user types quit, exit the program
print("Enter help for menu")
user_message = ""
is_started = False
while True:
    user_message = input("> ").lower()
    if user_message == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif user_message == "start":
        if is_started:
            print("The car is already started!")
        else:
            print("Car started")
            is_started = True
    elif user_message == "stop":
        if not is_started:
            print("The car is already stopped")
        else:
            print("Car stopped")
            is_started = False
    elif user_message == "quit":
        print("Exiting program")
        break
    else:
        print("Please enter a valid command")
'''
#######################################
# For loops
'''
for item in "Python":
    print(item)
for item in ["bob", "billy", "pop"]:
    print(item)
# Range function prints a range of values
for item in range(10):
    print(item)
prices = [10, 20, 30]
total = 0
for i in prices:
    total += i
print(f"Total = ${total}")
'''
###############################
# Nested loops
'''
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
# Print out F shape from list
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    output = ""
    for i in range(item):
        output += "x"
    print(output)
'''


######################################
# Tuple
'''
myTuple = tuple([0, 1, 2, 3])  # create tuple from list
myTuple.count(2)  # counts occurrences of given item in tuple
unpackTuple = 'bob', 'bobb'
name1, name2 = unpackTuple  # unpack items in tuple to variables
'''


########################################
# Sets: unordered, mutable, and have no duplicates
# provides union, intersection, and difference methods


########################################
# Functions
'''
def welcome_message(first, last):
    print(f"Hi {first} {last}")
    print("Welcome")
print("Start")
welcome_message("John", "Smith")
# Keyword argument
welcome_message(last="Smith", first="John")

def square(number):
    return number * number
square1 = square(3)
'''
########################################
# Exceptions
'''
# ValueError = type of error message
try:
    age = int(input("Age: "))
    print(age)
except = ZeroDivisionError:
    print("Age cant be 0")
except ValueError:
    print("Invalid value")
'''

