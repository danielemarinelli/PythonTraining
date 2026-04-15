#access from here module1 and module2 from same package
# NO problem, just import the modules
import module1
import module2

module1.display()
module2.show()

# if client is OUTSIDE the package, to import the modules we
# must specify the package name too (example in client1.py)

