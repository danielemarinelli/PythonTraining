# Mutable object --> can be changed after creation ( list, dict, set)
# Immutable object --> cannot be changed after creation ( int , float, tuple, str)

# Immutable
a1="school"
print(a1)
print(id(a1))   # mem location
print(a1[0])
#a1[0] = 'S'    --> TypeError: 'str' can't change the string directly because string is immutable
# same variable, but different memory location
a1='S'+a1[1:]
print(a1[1:])
print(a1)
print(id(a1))

# Mutable    (allow changes)
team=["j","u","v","e"]
print('orig list: ',team)
print("before mod: ",id(team))  # mem location same
team[0]='J'
print('modified list: ',team)
print("after mod: ",id(team))  # mem location same
