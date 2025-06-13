s1 = "Welcome "
s2 = "to Italy!!"
s3 = s1 + s2
print(s3)

s4 = s1*5
print(s4)
print(len(s4))

s5 = s1+str(2)
print(s5)

#membership operator
print("a" in s2)
print("Z" not in s2)

#Remove spaces
d = "  Daniele  "
print(d.rstrip())
print(d.lstrip())
print(d.strip())

#compare strings

print(ord("D"))  # returns the ASCII code
print(chr(89)) #returns the char of the ASCII inserted

f = "Marinelli"
r = "Marini"
print(ord("e"))
print(ord("i"))
print(f>r)

#find substrings
q= "Yesterday they elected the Pope. Everyone was very very very happy"
print(q.find("Pope")) #returns index
print(q.find("Java")) #returns -1
print(q.find("very")) #returns index
print(q.rfind("very")) #returns index of the last very
print(q.count("very"))
g = "I don't like ice-cream"
g1 = g.replace('ice-cream','broccoli')
print(g1)

#splitting and join
dat = "09-05-2025"
h = dat.split("-")
print(h)
p="%".join(h)
print(p)
p="/".join(h)
print(p)
p=" ".join(h)
print(p)


q= "Yesterday they elected the Pope. Everyone was very very very happy"
print(q.upper())
print(q.swapcase())

pope ="Leone XIV"
city = "Rome"
print(f"Yesterday they elected {pope}. Everyone was very very very happy in {city}")
print("Yesterday they elected {}. Everyone was very very very happy in {}".format(city, pope))