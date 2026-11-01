# count and Index()
t = 10,30,10,30,40,10,30,40,"sangha",40,3.10,3+3j,"sangha"
print(t,type(t))
t1=t.count(10) # counting the no of occurence of 10
print(t1,type(t1))
'''t2 =t.index(20) # ValueError: tuple.index(x): x not in tuple
print(t2)
'''
t3 = t.index(40) # returns the index of  specified value
print(t3)

for i,v in enumerate(t):
    print(i,"==>",v)