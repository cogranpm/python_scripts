""" input and output """

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
