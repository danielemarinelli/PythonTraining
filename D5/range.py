
print(list(range(10)))  #starting point 0, stop point n-1
print(list(range(4, 10)))
print(list(range(10,20,5)))  #(starting,stoping,step)
print(list(range(10,1,-1)))
print(list(range(-10,-2)))  # negative numbers

#for loop
for each_ele in range(1,11):
    print(each_ele)

#odd numbers
for x in range(1,21,2):
    print(x)

s="buongiorno"
for x in s:
    print(x)

for m in range(1,6):
    for n in (range(1,6)):
        print(f"{m} x {n} = {m*n}",end="\t")
    print()

for p in range(0,11,2):  # print even numbers
    print(p)
print("-->",p) #variable p is accessible even outside of the for loop


for b in range(1,7):
    pass   # for loop doesn't do anything
print("-->",b)


#break
for t in range(0,11):
    if t ==7:
        break   #terminate the loop
    print(t)

#continue
for t in range(1,11):
    if t ==5 or t ==6:
        continue  #skips the values, won't terminate the loop
    print(t)
