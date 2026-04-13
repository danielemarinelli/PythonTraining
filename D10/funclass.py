
# function with no parameters and no return value
def greetings():
    print("Hello, it's a sunny day!")

# calling the function outside the block
greetings()
greetings()
greetings()
print('<<<<<>>>>>>')

# function with one parameter and no return value
def day(name):
    print('have a great ',name)

day("monday")
day("Tuesday")

# function with 2 parameters and a return value
def calc(a,b):
   return a*b
value = calc(10,2)
print(value)

# function returns 'None' , 2 ways below:
def myfun():
    return
print('<<<<<>>>>>>')
print(myfun())
def myfun2():
    i =100
print(myfun2())
print('<<<<<>>>>>>')

#Arbitrary arguments
def sum_of_numbers(*numbers):
    tot = 0;
    for i in numbers:
        tot += i
    return tot

print(sum_of_numbers(1,2,3))
print(sum_of_numbers(2,30))
print(sum_of_numbers(2,30,9,13))
print(sum_of_numbers(21,330,90,173))
print('<<<<<>>>>>>')


def openfile():
    file = open('example.txt')
    #read file to output
    print(file.read())
    file.close()

openfile()