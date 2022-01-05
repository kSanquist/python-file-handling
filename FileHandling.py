# Kyle Sanquist
# 05 Jan 2022

# Used for exists() method to see if file exists
from os.path import exists, basename
import os

# Reads data from a file [size] characters at a time
def read_data(file_path, size):
    with open(file_path, 'r') as f:
        while(True):
            data = f.readlines(size)
            if len(data) < 1:
                break
            for line in data:
                print(line, end='')
    print('')

# Appends data to a file
# If a str of len 0 is entered, the loop for inputting ends
def append_data(file_path):
    with open(file_path, 'a') as f:
        print("Enter data, or type nothing to stop:")
        while(True):
            data = input("- ")
            if len(data) < 1:
                break
            f.write(data + "\n")

# Clears all data from file
# Uses truncate() to do so
def clear_data(file_path):
    with open(file_path, 'w') as f:  
        f.truncate(0)
        print('File cleared!')

# Creates a file, unless file already exists of course
def create_file(file_path):
    if exists(file_path) == True:
        print(f'{file_path} already exists and was not created')
    else:
        open(file_path, 'x')
        print('File created successfully!')

# Finds every instance of provided text and displays it
def find_text(text):
    appearances = []
    path = os.getcwd()
    for file in os.listdir(path):
        if file.endswith('.txt'):
            with open(os.path.join(path, file)) as f:
                lines = f.readlines()
                line_count = 0
                for line in lines:
                    line_count += 1
                    if text in line:
                        file_path = os.getcwd() + '/' + basename(f.name)
                        appearances.append([file_path, line_count, line[:-1]])
                    else:
                        continue
            line_count = 0
    # Checks to see if there are any instances to begin with
    if len(appearances) < 1:
        print("There were no instances of the provided text found.")
    else: 
        # Allows for nice displaying of instances
        counter = 0
        for list in appearances:
            counter += 1
            print('Instance %d:' % counter)
            print('Found in: ' + list[0])
            print('On line: ' + str(list[1]))
            print('Line:')
            print('"' + list[2] + '"')
            print()
