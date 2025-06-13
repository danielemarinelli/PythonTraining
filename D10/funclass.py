


def calc():
    a = 4
    b = 13
    return a*b

def openfile():
    file = open('example.txt')
    #read file to output
    print(file.read())
    file.close()



print(calc())
openfile()