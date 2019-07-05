# from the official python tutorials

#import for a deep copy
import copy
from math import pi

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
print("use collections.deque instead, fast appends and pops from both ends")
queue = deque(["winter", "summer", "spring", "autumn"])
queue.append("cold")
queue.append("warm")
queue.append("hot")
queue.append("wet")
print("queue starts as-: ", ", ".join(queue))
print("popping from left-: ", queue.popleft())
print("queue is now-: ", ", ".join(queue))
print("popping from right -: ", queue.pop())
print("queue is now-: ", ",".join(queue))

#list comprehensions
print("-------------------------------")
print("List Comprehensions")
print("non side effect method of creating a list in a loop")
print("Note:one way of doing this is using the factory method list, with parameter 1 being a function or lambda, parameter 2 an iterable")
print("eg: some_thing = list(map(lambda blah: blah, some_iterable))")
squares = list(map(lambda x: x**2, range(10)))
print("note: lambda used with map to convert list of ints to strings")
print("list of squares-: ", ", ".join(map(lambda x: str(x), squares)))
print("list comprehension method is more concise and readable and...")
print("brackets '[ ]', expression, for clause, then zero or more for or if clauses")
print("squares = [x**2 for x in range(10)]")
squares = [x**2 for x in range(10)]
print(squares)
print("combining two lists of items that don't match")
list1 = ["queen", "police", "ramones", "pistols"]
list2 = ["queen", "police", "ramones", "clash"]
newlist = [(x, y) for x in list1 for y in list2 if x != y]
print(newlist)
vec = [-4, -2, 0, 2, 4]
doublevec = [x *2 for x in vec]
print(doublevec)
non_neg_vec = [x for x in doublevec if x >= 0]
print(non_neg_vec)
print("apply function to all items")
func_vec = [abs(x) for x in doublevec]
print(func_vec)
print("creating list of tuples")
suites = ["spades", "clubs", "diamonds", "hearts"]
deck = [(suite, digit) for suite in suites for digit in range(1, 11)]
print(deck)
print("or  a list of tuples from a calc")
fun_list = [(x, x * 100) for x in range(5)]
print(fun_list)
print("list comprehensions can contain complex expressions and nested functions")
fun_list = [str(round(pi, i)) for i in range(1, 6)]
print(fun_list)
print("the expression in a comprehension can be any expression, including another list comprehension")
print("however beware of the complexity, use a built in function instead, such as zip()")

print("----------- the del statement -------------")
print("delete item by index, by slice, or entire list")
temp_list = ['a', 'b', 'c']
del temp_list[1:]
print (temp_list)
del temp_list

