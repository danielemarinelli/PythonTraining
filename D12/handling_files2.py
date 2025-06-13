#Handle binary files
#binary files --> rb,wb,ab,r+b,w+b,a+bf1 = open("draw-3583548_1280.jpg","rb")
f1 = open("draw-3583548_1280.jpg","rb")
print(f1.read())
bytes = f1.read()
f2 = open("draw-new.jpg","wb")
f2.write(bytes)
f1.close()
f2.close()

