import json
from pprint import pprint

#####################################
# Dictionary aka associative array / JSON at end
# unordered
# Key, value pairs

# Counting frequency of object
# Check if key is in dictionary
counts = dict()
names = ['cs', 'cw', 'cs', 'z', 'cw']

# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)
print()
# Alternative / Better approach
# get(keyname, default value): Returns the value of the item with the specified key.
for name in names:
    # add a new item or add 1 to an item
    counts[name] = counts.get(name, 0) + 1  # 0 provides a default value if key is not in dictionary
print(counts)
print()

# Counting pattern




customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# Prints the name of the customer
print(customer["name"])
print(customer.get("name"))
customer["name"] = "Jack Smith"

# Access key and value
myDict = {'name': 'Bob', 'age': 20}  # key, value pairs
print(myDict)
for key, value in myDict.items():
    print(key, value)

# String converter to list
# message = input(">")
# Split method splits the string by the given argument
# Space argument splits the words into a list of words
# words = message.split(" ")

print()
users = {'Bob': 'admin', "Tom": 'user', 'Paul': 'user'}
for user, privledge in users.copy().items():
    if privledge == 'admin':
        print(user)
print()

print('=====================================================')
##################################
# JSON
# Convert from JSON to Python w/ json.load() method
# Convert from python to JSON
print('JSON')

# Python object (dict)
json_dict = {'name': 'Bob', 'age': 28, 'city': 'clarksville'}

# Convert to JSON
json_convert = json.dumps(json_dict, indent=4)
print(json_convert)


print('=====================================================')
print('Dictionary pprint')
messy_dict = dict(z='Here is a really long key that spans a lot of text', a='here is another long key that is really too long',
                  j='this is the final key in this dictionary')

pprint(messy_dict)

print('=====================================================')
print('Dictionary get method while iterating')
people = ['Adam', 'Bella', 'Cara',
          'Adam', 'Bella', 'Cara',
          'Adam', 'Bella', 'Cara', ]

food = ['soup', 'bruschetta', 'calamari',  # starter
        'burger', 'calzone', 'pizza',  # main
        'coca-cola', 'fanta', 'water']  # drink

# Cost of each item in £
prices = [3.20, 4.50, 3.89,
          12.50, 15.00, 13.15,
          3.10, 2.95, 1.86]

# Zip data together to allow iteration
# We only need info about the person and the price
meal_data = zip(people, prices)
print('zip = ')

total = {}
for (person, price) in meal_data:
    # get method returns 0 the first time we call it
    # and returns the current value subsequent times
    total[person] = total.get(person, 0) + price

print(total)











