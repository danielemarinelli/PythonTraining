# Create/Write a file ( if file doesn't exist it will be created automatically in the folder
# PYTHON supports only TXT file build-in libraries
# to work with other files (excel...) 3rd party libs must be installed

# Before running this .py be sure that folder _ITALIAN_Music & file Italian_ROCK_music.txt don't exist

#Approach1
#file=open("C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\music.txt",'w')
#file.write("I love Dave Matthews Band type of music!")
#file.close()

#Approach2
with open("C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\Italian_music.txt","w") as file:
    file.write("I like Vasco Rossi and Ligabue's type of music!")
    file.close()

# Append data into file
file=open("C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\Italian_music.txt","a")
file.write("\n but even Litfiba is not bad at all")
file.close()

# Reading data from text file
#a) read()  -- all lines from file
#b) readline() -- read single line
#c) readlines() -- read all lines  into a LIST format
file=open("C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\Italian_music.txt","r")
#a) f=file.read()
#b) f=file.readline()
f=file.readlines()
print(f)
file.close()

# Rename the file
import os
original_file_name = "C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\Italian_music.txt"
new_file_name = "C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\Italian_ROCK_music.txt"
os.rename(original_file_name, new_file_name)
print("File renamed!!")

# Delete the file
import os
old_file = "C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\Italian_music.txt" #it's renamed so it does not exist
if os.path.exists(old_file):
    os.remove(old_file)
else:
    print("File doesn't exist")

# Create a directory
import os
dir_name = "C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\_ITA_Music"
os.mkdir(dir_name)
print("Directory created....")
if os.path.exists(dir_name):
    print("Directory exists")
else:
    print("Directory doesn't exist")


# Rename directory
import os
new_dir_name = "C:\\Users\\dmarinel\\PycharmProjects\\PythonSelenium\\_ITALIAN_Music"
os.rename(dir_name, new_dir_name)
print("Directory renamed....")

# Remove directory
import os
os.rmdir(new_dir_name)   # when folder it is empty
print("Empty Directory erased....")

#For non-empty folders, use:
#import shutil
#shutil.rmtree("folder_name not empty to delete")

import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

