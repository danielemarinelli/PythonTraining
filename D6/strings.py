s = "My name is Federica"
print(s)

r = """ Welcome to 
         my 
         house 
         in NYC"""

print(r)

name = str('Jimmy')
print(name)
print(type(name))

print(name+" the gymmy guy")  # concatenation
print(name * 4) #repeat

w = "Welcome to the 'Python' course"
print(w)

t = 'welcome to coding'
print(t[3])  #start index 0 ---> output 'c'
print(len(t))
print(t[-2])  # starting from the end with index -1 ---> output 'n'
print(t[3:14])  #substring
print(t[3:14:2])  #substring with step=2
print(t[:14:3])  #substring with step=3
print(t[::-1])  #reverse string direction
print(t[-2:-12:-1])
print(t[-4:-2])

age=45
#s='My age is'+age    #printing gives TypeError
s=f'My age is {age} years old'
print(s)

price=66    # price is number
st=f"The price is {price:.2f}"  # :.2f tells how many zeros to print
print(st)
st1=f"The price is {price * 3}"
print(st1)

# in  & not in return a boolean
print("pric" in st1)   #True
print("The" not in st1)  #False

c = 'ciao!'
print(c.capitalize())  #first characther uppercase

h = "Hello"
print(h.casefold())  # lowercase

v = "welcome to roma"
print(v.title())
print(v.upper())
vv = "Today It will rain"
print(vv.swapcase())

tt = "apple"
print(tt.center(10,'*'))

print("I love {}".format(tt))
print(tt.find("l")) #returns the index that starts from 0
print(tt.find("z")) #returns -1 if not found

