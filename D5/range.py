
print(list(range(10)))
print(list(range(10,20,5)))
print(list(range(10,1,-1)))

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