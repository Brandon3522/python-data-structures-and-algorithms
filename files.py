# file opening using with
# With closes the file automically, eliminating the need for exception handling for file close
# “r”  = If you want to read from a file.

# “w” = If you want to write to a file erasing completely previous data.

# “a” = If you want to append to previously written file.

# “x” = If you want just to create a file.
file_path = 'read_file_data.txt'
with open(file_path, 'w') as file:
    file.write('Age: 56\n')
    file.write('Hello\n')
    file.write('In file\n')

with open(file_path, 'r') as file:
    for line in file:
        lines = line.split()
    print(lines)


