# modules tutorial

import sys
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

import builtins

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
print("sys.path - gives you the python directory on your machine, and the place pip puts packages")
print("on my linux this is /usr/local/lib/python3.6/dist-packages/")
print(sys.path)
print("the directory containing the script being run is dynamically added to the search path")
print("you can add to this like this: sys.path.append('somedirectory')")

print("caching")
print("each module is cached under the __pycache__ directory")
print("the compiled version, which happens at runtime, is cached")
print("you can ship a 'compiled' version by removing source files and providing the compiled files")
print("the compileall module can create .pyc files for all modules in a directory")

print("-", "Standard Modules", "-")
print("the sys module is build into every python interpreter")
print("dir() function shows which names a module defines")
print(dir(fib))
print("call without arguments to show names currently defined: ", dir())

print("show the built in names of functions and variables: dir(builtins)")
print(dir(builtins))

print("packages are a way of structureing pythons module namespace by using dotted modules names")
print("a package is a collection of modules")
print("package is just a hierachy of directories each with it's own __init__.py file")

# import sound.effects.echo
# if you import this way you need to prefix with full names: sound.effects.echo.send_echo()
# or
from sound.effects import echo
print(echo.send_echo())
# you can also import the names of functions or variables directly:
# from sound.effects.echo import send_echo
# then the function name is available without prefix

print("importing * from a package")
print("in the __init__.py files, you can provide a list named __all__, it is taken to be the list of of modules names that should be imported when 'from package import * is encountered")
print("if it is not provided then it will only import what is in the __init__.py")
print("the recommended style is 'from package import specific_submodule'")
