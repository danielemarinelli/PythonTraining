#Creation TUPLE  (READ ONLY LIST!!!!!)
# IMMUTABLE OBJECT
t = () #empty tuple

print(t)
print(type(t))

t1 = (4)  #single value tuple
ts = 10,  #single value tuple
t2 =(8,9)
print(t2)
print(ts)

t3 = 9,4.6,True, "hello all"
t4 = tuple(range(15))   #Type casting
print(t3)
print(t4)

#t5 = eval(input('Enter data = '))
#print(t5)
#print(type(t5))

q= "Yesterday they elected the Pope. Everyone was very very very happy"
print(q.split())
print(type(q.split()))

q1= "Yesterday Juventus lost and everyone was very very very sad"
qt = tuple(q1.split())  #casting della lista in tupla
print(qt)
print(type(qt))

#Access data
# with index
print(qt[0])
print((qt[-7]))
# with slice operator
print((qt[3:6]))
print((qt[::-1])) #reverse

#Operator
print(t3+qt)
print(33 in t2)

#functions on Tuple
print(len(qt))
print(q1.count("very"))
print(q1.index("Juventus"))
print(sorted(q1))

#Tuple Comprehension NOT SUPPORTED IN PYTHON
pp = (x**2 for x in range(1,7))
print(pp)
print(list(pp))
print(type(pp))


teams=("lakers","Cavs","Celtics","Rockets","Nets","Knicks")
print(teams[2])
print(teams[1:4])
print(teams[-3:-1])
#change a value in tuple
# by default tuple is IMMUTABLE, we can't change value directly
# teams[3] = "Clippers"  NOT POSSIBLE/ERROR
# but if we cast into list, then we can change items
# tuple -> list -> tuple
print("before casting its a tuple (immutable)",teams)
teams_list = list(teams)
print("after casting its a list (mutable)",teams_list)
teams_list[3] = 'Scavolini'
print("after changing ",teams_list)
teams_tuple = tuple(teams_list)
print(teams_tuple)
print(len(teams_tuple))

#retrive items in tuple with loop
for i in teams_tuple:
    print(i)

if "cavolini" in teams_tuple:
    print("present!!")
else:
    print("not present!!")


#cannot add or remove values into a tuple because IMMUTABLE
#copy tuple
teams_tuple = teams
print(teams_tuple)
#join tuple
tuple1=(1,4,88)
tuple2=("Juve","Lazio")
tuple3=tuple1+tuple2
print(tuple3)
