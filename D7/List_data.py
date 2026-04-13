# a list is a collection which is ordered and changeable
# list is mutable

#create a list
list_1 = []  #empty list
print(type(list_1))
print(list_1)

list_2 = ["Daniele","Roma",30000,98.45,False,'Y']
print(list_2)
list_2[1]= "Urbino"   #change the item in the list
print(list_2)

#list_3 = eval(input("Enter any data you need: "))
#print(list_3)
#print(type(list_3))

q= "Yesterday they elected the Pope. Everyone was very very very happy"
list_4 = q.split(" ")
print(list_4)

print(list_4[-5])
print(list_2[0])
print(list_4[-1:-10:-1])
print(list_4[1:7:1])
list_4[0]="IERI"  # in the list I can change the data inside it
print(list_4)

for x in list_2:
    print(x)

if "Roma" in list_4:
    print("Yes, Roma is present")
else:
    print("No, Roma is NOT present")
print("len list_4: ",len(list_4))
print('how many times VERY is repeated: ',list_4.count("very"))
list_4.sort()    #elements in ascending order
print(list_4)
list_4.sort(reverse=True)    #elements in descending order
print(list_4)

list_5 =[20,40,60,60,80,50,60]
print(len(list_5))
print(list_5.count(60))
list_5.append(100)   # insert at last position
print(list_5)
list_5.remove(60)
print(list_5) #removed only the first 60
list_5.sort()
print(list_5)

#REVERSE LIST (values must be in sorted order)
cities= ["Bologna", "Cagliari", "Firenze", "Torino", "Udine"]
print("Original -->",cities)
cities.reverse()
print("Reversed -->",cities)
# Add item  append() and insert()
cities.append("Urbino")
cities.append("Pesaro")
print(cities)
cities.insert(3,"Ascoli")
print(cities)
# remove items from list
teams=["lakers","Cavs","Celtics"]
print(teams)
teams.remove("Celtics")
print(teams)
teams.append("Mavs")
print(teams)
teams.pop(1)
print(teams)
teams.pop(0)
print(teams)
#delete permanently the list
del teams


# Copying a list first approach
fruits=["banana", "grape","mango"]
fruits_new=fruits.copy()
print(fruits_new)
print(fruits)
# Copying a list 2nd approach
jobs=["QA","dev","PM","ProdOwner"]
jobs_new=list(jobs)
print(jobs_new)
print(jobs)

# Join list , three ways
Job = jobs+jobs_new
print("with + ",Job)

for i in jobs:
    jobs_new.append(i)
print("with FOR loop ",jobs_new)

jobs_new.extend(jobs)
print("with extend method ",jobs_new)