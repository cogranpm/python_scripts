# modules tutorial
import fib #use the module name to call the functions

# other method of import, no module prefix required to call
from fibo import fib3

# you can import all names (except those beginning with underscore) like this:
# from fibo import *

# import via alias
import fibo2 as fib2

# import via alias with from form
from fibo3 import fib3 as fibonacci

# module only loaded 1 per interpreter session
import importlib

fib.fib(1000)
print(fib.__name__)
print(fib3(300))
print(fib2.fib(0))
print(fib2._private_fib(0))
print(fibonacci(3))

print("use importlib.reload(modulename) to reload a module")
importlib.reload(fib)
print("note that you can't reload unless you imported like: import modulename")
#importlib.reload(fibo)

print("add an if statement to have script run as importable module OR a script")
print("if __name__ == '__main__':")
print("this if module is imported, as opposed to run as a script, the 'main' bit won't execute")
print("-" * 10, "module search path", "-" * 10)

