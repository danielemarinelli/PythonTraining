
# try except block (open a file that does not exists)
try:
    with open('filelog.txt','r') as reader:
        reader.read()
except:
    print("Something went wrong somewhere") #customize msg error
#---------------------------------------------
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)  # python error display

finally:
    print("Finished!!!!")  # line always executed


# nested try-catch blocks
# one example is line 23 without specify the mode (external exception will run)
# another example is -> change mode from w to r  (nested exception will run)
try:
    file=open('filelog.txt','w')
    try:
        file.write("hello world")
    except:
        print("Something went wrong when writing to file")
    finally:
        file.close()
except:
    print("Something went wrong when opening the file")



