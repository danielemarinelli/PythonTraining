# how to access CLASSES into different modules

#Approach 1 no problem
#import aa
#import bb

#obja = aa.Animal()
#obja.display()

#objb = bb.Bird()
#objb.display()


#Approach 2 no problem - preferred
from aa import Animal   # import the module and then use the classes
from bb import Bird
objanimal = Animal()
objanimal.display()
objbird = Bird()
objbird.display()

