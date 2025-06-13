#Creation TUPLE  (READ ONLY LIST!!!!!)

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
