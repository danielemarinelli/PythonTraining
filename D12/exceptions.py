#Exceptions

#x=6
#res=6/0  Exception ---> ZeroDivisionError
#print(res)

print("start!!")
x="10"
#print(x+5)  another exception: add string and num not possible

try:
    print(x+5)
except:
    print("An exception occured...")
print("finish!!")


# Multiple exceptions

try:
    print(abc)
except NameError:
    print("Variable abc is not defined...")
except:
    print("other exceptions...")

# Try block with else

try:
    print("Checking exceptions")
    100/0
except:
    print("something went wrong...")
else:
    print("Nothing went wrong today")


# Finally keyword
try:
    print(b)
except:
    print("something went wrong again...!!!")
finally:   # finally block always is executed
    print("here is the finally block")

# combination try, except, else, finally
try:
    n=int(input("Enter a value: "))
    res=100/n
except ZeroDivisionError:
    print("Don't divide by Zero....")
except ValueError:
    print("Enter a valid number...")
else:
    print(res)
finally:
    print("Exceptions completed!!")





#####################################
ItemsInCart = 0
# 2 items will be added in cart from automation script
# with raise keyword you can send your own exception (mostly developers use it)
if ItemsInCart !=2:
    raise Exception("ItemsInCart must be 2.....")




