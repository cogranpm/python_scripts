print("objects have a type, identity and value, eg someid = 5, has type integer, identity = someid and value = 5")
someid = 5
print("id() gives identity of object as an integer: ", id(someid))
print("the is operator compares identity of two objects")
otherid = 5
dupedid = someid
print("someid is dupedid: ", someid is dupedid)
print("someid is otherid: ", someid is otherid)
print("== compares values, not idenity")
print("someid == otherid", someid == otherid)
print("type() functions gives type of an object: ", type(someid))
somestr = "I am string"
somedec = 48.7
somelist = ['a', 'b', 'c']
somedict = {1: "fred", 2: "steven", 3: "malcolm"}
someset = {1, 2, 3}
sometuple = ("fred", "smith")
print(type(somestr), type(somedec), type(somelist), type(somedict), type(someset), type(sometuple))
print("types can be compared, all type objects are assigned names such as list, dict and file")
print("type(somelist) is list: ", type(somelist) is list)
print("type(somedict) is dict: ", type(somedict) is dict)
print("type(somestr) is str: ", type(somestr) is str)
print("isinstance() is a safer way to check types, eg isinstance(somelist, list)")
print(isinstance(somelist, list))


print("-" * 10)
print("reference counting and garbage collection")
print("del statement decreases reference count")

