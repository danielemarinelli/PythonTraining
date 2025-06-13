#create a list
list_1 = []  #empty list
print(type(list_1))
print(list_1)

list_2 = ["Daniele","Roma",30000,98.45]
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

list_5 =[20,40,60,60,80,50,60]
print(len(list_5))
print(list_5.count(60))
list_5.append(100)
print(list_5)
list_5.remove(60)
print(list_5) #removed only the first 60
list_5.sort()
print(list_5)