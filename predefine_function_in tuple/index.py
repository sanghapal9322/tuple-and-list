a = 20,30,40,30,"python"
print(a,type(a))
b = a.index(30)
print(b)

c = a.index(100)
print(c)

#1) index()
tup = (1,2,3,4,("pyhton","Guido"),(" van russom","sanghapal"))
for val in tup:
    print(f"{val}==>{type(val)}")