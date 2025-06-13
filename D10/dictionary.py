
d = {}  #empty dict
dd = dict()   #empty dict
print()
print(type(d))
print(type(dd))

d = {10:"Fede", 20:"May", 30:"Juan",40:"Maria"}
print(d)

print(d[10]) #Access dict's data

#del d[40]
#print(d)

print(len(d))
#d.clear()
#print(d)
print(d.keys())
print(d.values())
print(d.get(30))
print(d.get(3000))

print(d.pop(40)) #remove the entry of the key specified
print(d)

d2 = d.copy()
print(d2)

print(d.items())
d.update({1:'Ale',2:'Edo',3:'Rose'})
print(d)
print(d.items())

word = 'mississippi'
d3 = {}

for x in word:
    d3[x] = d3.get(x,0)+1

print(d3)

for k,v in d3.items():
    print(k,"occured",v,"times")