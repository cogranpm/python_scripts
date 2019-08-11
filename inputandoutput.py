""" input and output """
import math

print("fancier output formatting")
print("formatted literal strings: f'text text {variable} {variable}'")
year = 1999
month = "November"
print(f"The year was {year} and the month was {month}")
myformattedstring = F"The year was {year} and the month was {month}"
print(myformattedstring)
print("str.format() method where str is a string")
some_fraction = 23 / 7
print(some_fraction)
print("the fraction is {:.4}".format(some_fraction))
print('-' * 10)
print('basic usage')
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('you can put a number in the { } s')
print('{0} and {1}'.format('spam', 'eggs'))
print('you can put keyword args in the { } s')
print('This {food} is {adjective}.'.format(food='spam', adjective='shit'))
print('you can mix and match index and keywords')
print('pass a dict and use in format')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
print('there is a ** notation when using a dict, eg "something{key}".format(**somedict)')
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print(" print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))")
print(" the 0 in {0:2d} is the minimum width, the 2 is decimal precision")

print("-" * 10)
print("manual string formatting")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))


print('old skool string formatting uses % operator')
print('pi is %5.3f.' % math.pi)

print('reading and writing files')
print(' obj = open(filename, mode), r is the default')
print("possible modes: 'r', 'w' (erases existing), 'a' (append), 'r+' (read and write)")
