#Approach1 , no problem
import animal
import bird

animal.fly()
animal.color()

bird.color()
bird.fly()

#-------------------------------
#Approach 2 if duplicate names methods this is the solution

from bird import *
fly()
color()

from animal import *
fly()
color()
