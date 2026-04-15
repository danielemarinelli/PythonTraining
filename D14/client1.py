# Approach1
#import pack1.module1
#import pack1.module2

#pack1.module1.display()
#pack1.module2.show()

# Approach2  ---> more convenient
from pack1.module1 import *
from pack1.module2 import *
display()
show()



