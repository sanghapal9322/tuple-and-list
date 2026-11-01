# lst obj = sorted(iterable object)
tup = (20,30,89,83,200,34)
print(tup,type(tup),id(tup))
lst =sorted(tup)
tup = lst
print(tup,type(tup),id(tup))