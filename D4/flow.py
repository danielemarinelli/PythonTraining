
name = input("Enter your name: ")

if name == "Daniele":
    print("Good morning Daniele, happy coding!")
elif name == "Federica":
    print("Good morning Federica, how are you today?")
elif name == "Alessandro":
    print("Good morning Alessandro, go to school!")
else:
    print("Hello guest, what is your name?")


y = input("Enter a number: ")
num = int(y)
if num%2==0:
    print("Number inserted is even!!")
else:
    print("Number inserted is odd!!")

i=1
while i<=4:
    print(i)
    i=i+1

name=""
while name!="Daniele":
    name=input("Enter your name please: ")
print("Thanks for checking in Daniele")

# Discount
amount = int(input("Enter your amount: "))
if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
    discount = amount * 10 / 100
elif amount > 1000:
    discount = amount * 5 / 100
else:
    discount=0

print("Your discount is:", discount)
print("Payment amount after discount: ",amount-discount)