#Type of arguments
#Positional arguments

def divis(i,j):
    print(i/j)
#order matters
divis(2,3)
divis(3,2)

#---------------------
# Keyword arguments
#order does not matter
divis(i=12,j=6)
divis(j=6,i=12)


def wish(name,msg):
    print("Hello", name,msg)

wish("Federica",msg= "You are beautiful")

#----------------
#default arguments

def wish(name="Daniele",msg=" it's late!!"):
    print("Hello", name,msg)

wish()
wish("Alessandro", msg="Good morning!!")

#----------------------
#Variable Length Arguments
def sum(*n):
    print (n)

sum()
sum(3)
sum(20,40)
sum (5,9,12)

#----------------------
#Keyword Variable Length Arguments

def display(**kwargs):
    for key, value in kwargs.items():
        print (key,"=", value)
    print(kwargs)

display(a=3,b=4)
display(i=300,j=400,k=500)

def create_user_profile(name, age, **additional_info):  # ** variable length arguments!!
    profile = {"Name": name, "Age": age}  #dictionary
    profile.update(additional_info)  # add additional information to the profile
    print("User Profile:::==>> ",profile)
    print(profile["Name"])

create_user_profile("Daniele","46", location="Buffalo", profession="Python Tester", hobbies="NFL")
create_user_profile("Federica","45", profession="Cuoca")















