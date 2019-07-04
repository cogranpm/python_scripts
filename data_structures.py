# from the official python tutorials

#import for a deep copy
import copy

#import for a queue structure
from collections import deque

a = ['one', 'two', 'three']
a.append('four')
print(a)
#insert at front of list
a.insert(0, 'zero')
print(a)
# append another list ie cons
b = ['five', 'six']
a.extend(b)
print(a)
# remove by value
a.remove('six')
print(a)
# pop the last item
print(a.pop())
print(a)
#pop at index
print(a.pop(2))
print(a)
a.clear()
print(a)
a = ['kill buffer', 'show buffer list', 'create, switch buffer']
print(a)
# index, where value is in list
print(a.index('show buffer list'))
#lets get some data into a list
file_contents = []
with open('gk-dickens.txt', 'rt') as f:
    for line in f:
        file_contents.append(line.strip())

# get get a VallueError if item not in list
try:
    index_of_swiveller = file_contents.index('Swiveller')
    print(index_of_swiveller)
except ValueError:
    print('item not lin list')

print('g k exists this many times in file: ', file_contents.count('G. K. CHESTERTON'))

#look at some random section of the list
for line in file_contents[0:10]:
    print(line)

#sorting a list, mutates the list in place
a.sort()
print(a)
a.reverse()
print(a)
# another way, sorted accepts any iterable, including your own classes if designed with iteration in mind
bsort = sorted(a)
bsort.append("I was sorted")
print(bsort)
print("----------------------")
print("lower case sort example")
wlist = ['Tom Sawyer', 'tom sawyer', 'Huck Finn', 'huck finn']
# key is a function to be called on each element prior to comparing
print(sorted(wlist, key=str.lower))
print('without key sorting')
print(sorted(wlist))
# more complex example with a tuple list
# note that the "key" argument to sorted is a lambda function which takes the list item as parameter and returns a string
zlist = [ ('hawthorn', 'full forward', 'dunstall'), ('essendon', 'full forward', 'madden'), ('carlton', 'full forward', 'kernahan')]
print('sort tuple by first item in record, which is club name')
print(sorted(zlist, key=lambda record: record[0]))



#what's a shallow copy of a list, shallow copy means a new list, but it has references to items in the list
# change an item in the list and it changes the original
acopy = a.copy()
acopy.pop(1)
print(acopy)
print(a)
# another way to copy is
bcopy = a[:]
bcopy.append("I'm different")
bcopy[0] = "malcolm"
print(bcopy)
print("is the original first item changed to malcolm? ")
print(a)
# here is how to do a deep copy
ccopy = copy.deepcopy(a)
ccopy.append("I am deep")
print("this is the deep copy, you can change items ")
print(ccopy)
print("---- this is the original ------")
print(a)
ccopy[0] = "fred"
print("--------- changed first item -----------")
print(ccopy)
print("---------- this is the original -------")
print(a)
# here is the pythonic way to copy a collection, use the factory function
print("------ using factory function to copy list x = list(y) ---------")
dcopy = list(ccopy)
print(dcopy)


#using lists as stacks etc
print("use the pop() function on list to emulate a stack, returns last item added")
print("do not use a list to emulate a queue because 'popping' first item is slow")
print("use collections.deque instead")
queue = deque(["winter", "summer", "spring", "autumn"])
