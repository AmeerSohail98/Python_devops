# Creating a python program to take folder name as input and 
# check all the folders present in it and display all the file names present in the folders
import os
folders = input('Please provide the list of folders names with spaces in between:' ).split()

for folder in folders:
    try: # Exception handling
        files=os.listdir(folder)
        print("-->List files in the present folder:",folder)
        for file in files:
            print(file)
    except FileNotFoundError:
        print('Provide a valid file name')
        continue
    # print("-->List files in the present folder:",folder)
    # for file in files:
    #     print(file)
    