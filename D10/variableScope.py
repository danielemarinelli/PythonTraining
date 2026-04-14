# variables created OUTSIDE a function are GLOBAL VARIABLES
# variables created INSIDE a function are LOCAL VARIABLES

a = 100
def myfunc():
    b=30
    print(a)
    print(b)
myfunc()  # Global and local are accessible inside a function

print(a)  # OK
#print(b) ERROR!! its local variable

#-------- Example of Global and Local Variable with SAME NAME

x = 10
def myfunc1():
    x = 9
    print("local ",x)

myfunc1()
print("global ",x)


#-------- Example UPDATE the global variable inside a function
m =99
def myfunc2():
    global m    # use keyword GLOBAL
    m=222
    print("updated GLOBAL variable from a function",m)
myfunc2()

print(m)

#-------- Example Declare a GLOBAL variable inside a function
def myfunc3():
    global k
    k=400
    # in one line is syntax error
    # global k =400
    print(k)
myfunc3()
print(k)




