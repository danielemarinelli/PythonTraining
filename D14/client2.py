# access all three modules from client2 outside the 2 packages
#approach1
#import pack1.module1
#import pack1.module2
#import pack1.pack2.module3

#pack1.module1.display()
#pack1.module2.show()
#pack1.pack2.module3.show_child()

#approach2
#from pack1 import module1
#from pack1 import module2
#from pack1.pack2 import module3

#module1.display()
#module2.show()
#module3.show_child()

#approach3
from pack1.module1 import *
from pack1.module2 import *
from pack1.pack2.module3 import *
display()
show()
show_child()

# DIRECTORY is only a folder and all the modules/file.py inside can't be accessed
# PACKAGES contain modules/file.py, they can be imported from all the project

