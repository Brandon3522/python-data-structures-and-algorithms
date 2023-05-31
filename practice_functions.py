

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(f"{number} Is not divisible by either 3 or 5")

print(fizz_buzz(30))

# for every 5 over 70 = 1 point
def speed_check(speed):
    points = 0
    if speed < 70:
        print("Ok")
    elif speed > 70:
        if points > 12:
            print("Suspended")


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


print(" ")
# 2D array testing
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[0][1])
# Print all numbers in matrix
for row in matrix:
    for item in row:
        print(item)

print('========================================================================')
# for loops
# i is the index
for i in range(len('bob')):
    print(i)
print()

# i is value
for i in 'bob':
    print(i)
print()

# index and value
for i, val in enumerate('bob'):
    print(f'{i}: {val}')
print()

testList = [0,2,3,5,9,40]
for i in range(len(testList)):
    val = testList[i]
    print(f'i: {i}     val: {val}')

print('========================================================================')
# list comprehension
# new_list = [expression for member in iterable]
squares = [i * i for i in range(10)]
print(f'Squares: {squares}')

# Same: for loop variation
squares1 = []
for i in range(10):
    squares1.append(i * i)
print(f'Squares 1: {squares1}')

# Compute factorial
def my_factorial(n):
    if n == 1:
        return 1
    else:
        return n * my_factorial(n - 1)

my_factorialResult = my_factorial(25)
print(f'My factorial: {my_factorialResult}')


