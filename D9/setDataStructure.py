# creation of Set Objects
s = set()    #empty setData Structure
print(type(s))

s1 = {3,True,8.99,"Hello",5+6j} #Order changes
print(s1)
print(type(s1))

s2 = {33,True,4.99,"Hello Loe","Hello Loe", 33}
print(s2) #Unique values, No doubles are displayed

#functions on SET
s3 = {10,6,99,50,30,78}
print(s3)
#s3.add(88) #one element
s3.update([100,200,300,400]) #more elements to add
print(s3)
s4 = s3.copy()
print(s4)
s5 = {10,6,99,50,30,78}
s5.pop()   #removes random element
print(s5)
print(s5.discard(99))
#s5.clear()
#print(s5)

#operations in SET
s6 = s5.union(s1)
print(s6)

x = {1,3,5,6,9}
y = {1,2,7,9}
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))
print(x.symmetric_difference(y))

s7 = {2**x for x in range(7)}
print(s7)









