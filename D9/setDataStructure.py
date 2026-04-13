# creation of Set Objects  - DUPLICATES NOT ALLOWED
s = set()    #empty set and it is MUTABLE OBJECT
print(type(s))

s1 = {3,True,8.99,"Hello",5+6j} #Order changes UNORDERED LIST
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
print(x.intersection(y))  # common values in sets
print(x.difference(y))
print(y.difference(x))
print(x.symmetric_difference(y))

s7 = {2**x for x in range(7)}
print(s7)

#ONLY WAY TO ACCESS ITEMS IN SET is with loop
for i in s2:
    print(i)

#search an item in SET
print("Hello Jon" in s2)  # False

if "Hello Loe" in s2:
    print("Yezzzz")
else:
    print("Nope!!")

print(len(s2))
# sorting, reverse, count of duplicates NOT possible

#ADD items in SET  --
# add() for one item or update() for multiple items to add

s6.add('Panama')
print("AFTER ADD()", s6)

s6.update(['English','QA Engineer'])
print("AFTER UPDATE()", s6)
#REMOVE ITEMS (three ways)
# with remove()
s6.remove('English') #if item not present in tuple will receive KeyError:
print("remove()", s6)

# with discard()
s6.discard(78)  #if item not present in tuple , no error will be shown
print("discard()", s6)

# with pop()  removes random value from the set
s6.pop()
print("pop()", s6)
s6.pop()
print("2nd pop()", s6)
s6.pop()
print("3rd pop()", s6)
s6.pop()
print("4th pop()", s6)

#clearing values from  set:
g = {'Chelsea','United States','Liverpool'}
g.clear()
print("After clear() --> ",g)

del g
#print("After del) --> ",g)  #NameError:

# COPY a SET in 2 ways, with set() or with copy()
s2=set(s6)
print(s2)
print(s6)

t1={'G','I','Joe'}
t2=t1.copy()
print(t2)
print(t1)

# Joining of sets using union() or using pipe | symbol
m1={'w','p'}
m2={9,4}
m3=m1.union(m2)
print("with union() ",m3)
m3.clear()
m3=m1 | m2
print("with pipe | ",m3)


