
# Read a file
try:
    file_handle = open('read_file_data.txt', 'r')
except FileNotFoundError:
    print('File not found')
    quit()

for line in file_handle:
    line = line.rstrip()  # Removes /n from file
    if line.startswith('Name:'):
        print(line)

# Alternative method
for line in file_handle:
    line = line.rstrip()  # Removes /n from file
    if 'Name:' not in line:
        continue
    print(line)



