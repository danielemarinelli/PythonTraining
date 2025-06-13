f = open("abcd.txt","r")
print(f.tell()) #where is my cursor positionated?
                #index of first char is  =  0
print(f.read(2)) #read first two positions
print(f.tell())
f.seek(0)  #posiziona il cursore all'inizio
print(f.tell())
f.close()

