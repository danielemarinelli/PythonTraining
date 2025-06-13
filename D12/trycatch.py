
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
    print(e)  # python error displyed

finally:
    print("Finished!!!!")  # line always executed
