# store data values in key:value pairs
# Dict is ORDERED, MUTABLE, no DUPLICATION
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

# similar to JSON
myd = dict(name="James",lastname="Bond",id="007",job="Actor")
print(myd)

myd1 ={
    "name": "James",
    "lastname": "Bond",
    "age": 36,
    "job": "Actor",
    "movies": ["goldfinger","skyfall","spectre"]
}
print(myd1)

# Retrieve values must know KEY
print(myd1["job"])
print(myd1.get("movies"))
print(myd1.get("age"))
# Retrieve only KEYS or only VALUES
print(myd1.keys())   # keys are unique, not duplicated
print(myd1.values())  # values can be duplicated

# retrieve all items: RETURNS couple of lists
print(myd1.items())

d = {10:"Fede", 20:"May", 30:"Juan",40:"Maria"}
if "20" in d:   # only KEYS we can check if present or not
    print("Key is present")
else: print("Key is not present")

if 20 in d:   # only KEYS we can check if present or not
    print("Key is present")
else: print("Key is not present")

# Add new item at the end
d["kids"]=True
print("Added new item ",d)
# Add update item
d[20]="Urbino"
print(d)
d.update({"kids":False})
print("after update ",d)

#REMOVE items k,v  , three ways:
print("original dict --> ",myd1)
myd1.pop("name")  # specify the key
print(myd1)
myd1.popitem()  # removes the last item of dict
print(myd1)
del myd1["age"]
print("item age gone",myd1)
# remove all items , but keep dict empty
myd1.clear()
print("clear method ->",myd1)
del myd1  # delete all items plus the dict too
#print(myd1) ---> gives #NameError:

# copying with copy()
df=d.copy()
print(df)
print(d)
print("length",len(d))  #length

#Retrieve all KEYS in dict
for k in d:
    print(k)
for k in d.keys():
    print(k)

print("-----")
# Retrieve all VALUES in dict
for v in d.values():
    print(v)

# Print all items from the dict
for k,v in d.items():
    print(k,v)

