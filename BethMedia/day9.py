print()

print()

# Opening and Reading Files..

# using the open() function

'''
file_object = open('filename', 'mode')
'''

'''
common modes
r read mode
w  write mode
a append mode
x   exclusive creation
b binary mode
t text mode
'''
# ********************************************************
print()

#   open the file in read mode
file = open("example.txt", 'r')
# Read content of the file
content = file.read()
# Print the content
print(content)
# Close the file
file.close()

print()

# ********************************************************

# Reading line by line
print()

#   open the file in read mode
file = open("example.txt", 'r')
# read each line one by one
for line in file:
    print(line.strip())  # strip removes newline characters
# close the file
file.close()

# ********************************************************

# Using readlines
print()
#   open the file in read mode
file = open("example.txt", 'r')
#   Read all lines into a list
lines = file.readlines()
print(lines)

#   Print each line from the list
for line in lines:
    print(line.strip())
# close the file
file.close()
print()

# ********************************************************
# Writing to files ( w write)
#   step 3
#   open the file in write mode (creates a  new file if it does nt exist)
file = open("output.txt", 'w')
#   write data to the file
file.write("Hello, world\n")
file.write('This is a new line.\n')

# close the file
file.close()

# ********************************************************
# Appending to files (a mode)
#   open the file in append mode
file = open("output.txt", 'w')

#   Add new context to the file
file.write('This line is appended.\n')

# close the file
file.close()

# ********************************************************
# To avoid forgetting to close files manually , you can use the statement,which autmatically handles files closing

# # using the wih statement
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed at the end of the block

# ********************************************************
# Working with binary files

# Open an image file in binary mode
with open('cover_photo.jpg', 'rb') as file:
    binary_data = file.read()
    print(binary_data)

# ********************************************************
# handling file exceptions

try:
    with open('non-existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not Found. Please check the filename.')

# ********************************************************

'''

Practice Questions

1. Write a Python program that prompts the user for their name and age, then writes this information to a file called user _info txt. The file should be created (or overwritten) if it already exists.
2. Create a Python program that opens a file called story.txt, counts the number of words in the file, and prints the total word count.
3. Write a Python program that reads a CSV file called students.csv that contains names and grades of students. Then, write another file called
student_results.csv that appends the result of whether the student passed or failed. Assume that a score of 50 or above is a pass.

'''
