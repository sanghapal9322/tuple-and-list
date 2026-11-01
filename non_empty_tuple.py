''' synatax = : tupleobject = (value1,valu2------valu-n)
    Syntax 2 =: tupleobject = value1,value2------valu-n
    Syntax 3 =: tupleobject = tuple()
    Syntax 4 =: tupleobject = noniterable,
'''
numbers = (10,20,30,40,50)
print(numbers,type(numbers),len(numbers),id(numbers))
'''numbers[0]=100
print(numbers) #TypeError: 'tuple' object does not support item assignment
'''
print("="*90)
print("synatax = : tupleobject = (value1,valu2------valu-n)")
t = ("sangha",30,3.14,3+34j,33)
print(t,type(t),len(t),id(t))
print("="*90)

m = 20,30,3.13,"sangha"
print(m,type(m),len(m),id(m))
print("="*90)
lst = [10,20,30,"sangha"]
tup = tuple(lst)
print(tup,type(tup),id(tup))

print("="*90)

string = "sangha"
st = tuple(string) # str to tuple
print(st,type(st),len(st))
l1 = list(st) # tuple to list
print(l1,type(l1),len(l1))

print("="*90)
k = (90)
print(k,type(k))

k1 = (900,)
print(k1,type(k1),len(k1))

print("="*90)

z = 10,
print(z,type(z))