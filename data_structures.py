# from the official python tutorials
# data structures chapter
#import for a deep copy
import copy
from math import pi

print("-" * 10, "Data Structures", "-" * 10)


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

#tuples and sequences
print("tuple is a number of values seperated by comma: t = 123, 456, 789")
print("you can mix and match types in a tuple")
mytuple = "fred", "barney", "wilma"
print(mytuple[0])
tupleintuple = "score", (5, 7, 90)
print("embedded tuple: ", tupleintuple)
#list inside a tuple, is it mutable
mylisttuple = ['a', 'b', 'c'], [1,2,3]
print(mylisttuple, "now I will delete the 'c'")
del mylisttuple[0][2]
print (mylisttuple)
#unpacking a tuple
a, b, c = 'a', 'b', 'c'
print(a, b, c)
#unpacking works with lists, etc too
a, b, c = ['z', 'x', 'y']
print(a, b, c)
#empty tuple
myempty = ()
mysingle = 1,
print(myempty, mysingle)

print("sets are unordered collection with no duplicates, use factory method or {} ")
basket = {'apple', 'orange', 'pear', 'orange'}
print(basket)
print("fast membership testing via in, eg 'pear' in basket", 'pear' in basket)
myemptyset = set()
print("use set() for empty: ", myemptyset)
a = set('abracadabra')
b = set('alacazam')
print(a, b)
print("a - b, what is in a but not b : difference:", a -b)
print("a | b, in a or b or both: ", a | b)
print("a & b, in both a and b: ", a & b)
print("a ^ b, in a or b but not both: ", a ^ b)
#set comprehensions
mynewset = {x for x in 'abracadabra' if x not in 'abc'}
print("set comprehension: { statement for clause if clause }:", mynewset)
print("set comprehensions use squiggly braces, which are also used by dictionaries ")

#Dictionaries
print("Dictionaries, keys must be immutable, like numbers and strings")
print("Tuples can be keys if elements are immutable")
mymtdict = {}
print("Empty dict: ", mymtdict)
print("it is an error to extract a value using non existent key")
print("performing list(d) where d is a dict returns a list of all keys")
print("for a sorted list of keys use sorted(d) where d is a dict")
print("to check if item in dict use the in keyword")
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print("list of keys: ", list(tel))
print("sorted list of keys: ", sorted(tel))
print("using in to check key: ", 'jack' in tel)
print("mix with not in: ", 'jack' not in tel)
print("factory method is dict, passed sequences of key-value pairs, think list of tuples")
print("dict([('dingo': 1111), ('rasha': 2222)])")
somedict = dict([('dingo', 1111), ('rasha', 2222)])
print(somedict)
print("also can use dict comprehensions to build key and value expressions")
compdict = {x: x**2 for x in (2, 4, 6)}
print("dict comprehensions: {key: value for clause if clause}")
print(compdict)
print("when keys are simple strings, use keyword argument style: dict(dingo='dog', redbelly='snake')")
ozdict = dict(dingo='dog', redbelly='snake', redback='spider')
print(ozdict)
print("Dingo is a: ", ozdict.get('dingo'))
print("items() method gives you key and value at same time")
for animal, species in ozdict.items():
    print(animal, ":", species)

print("enumerate library function (ie not an object method on a dict) gives the index and the value")
print("pass it the sequence to enumerate as an argument")
for index, species in enumerate(ozdict):
    print("species at ", index, "is", species)

print("zip allows to loop over 2 or more sequences at same time")
questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))


print("to loop in reverse order, use reversed() providing a sequence as the argument")
for a in reversed(sorted(questions)):
    print(a)

print("remember, to eliminate dups, can cell set() factory method passing a list")
print(set(['apples', 'oranges', 'potatoes', 'oranges']))
print("remember, don't mutate list during loop, create a new one instead")
players = ['dunstall', 'platten', 'rioli', 'jezza']
hawks = []
for p in players:
    if not p == 'jezza':
        hawks.append(p)
print(hawks)
print("sequences may be compared using standard operators: eg < > ==")
print("This completes the official tutorial on data structures")



