
f = open("abcd.txt", "w") # write mode
# Properties of a file
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)

#write data to a file
f = open("abcd.txt", "w") # write mode DATA WILL BE OVER WRITTEN
f.write("The train is late!!\n")
f.write("And I am tired.\n")
f.close()
f = open("abcd.txt", "a") # APPEND MODE!! wont' overwrite
list = ["and it is cold\n","I forgot the phone\n"]
f.writelines(list)
f.close()

#read data from file
f = open("abcd.txt", "r") # read mode
#print(f.read())
print("<<>>")
print(f.read(10))  # read only the first 10 chars
f.close()

f = open("abcd.txt", "r") # read mode
lines = f.readlines()
print(lines)
print(lines[1]) # read only line index = 1
print(lines[1:2])  # read lines in range of lines
f.close()
#IF I FORGET TO CLOSE THE FILE with close() might have problems
# we can close file automatically once the operation is performed with
# this code below ('with statement'):
with open("fghi.txt", "w") as f:
    f.write("File\n")
    f.write("Handling\n")
    f.write("Session\n")
    print("is file closed inside with loop: ", f.closed)
print("is file closed inside with loop: ",f.closed)


#check if a file exists or not
import os
filepath = r"C:\Users\dmarinel\PycharmProjects\PythonSelenium\D11\abcd.txt"
print(os.path.isfile(filepath))
print(os.path.exists(filepath))
#print(Path(filepath).exists())





