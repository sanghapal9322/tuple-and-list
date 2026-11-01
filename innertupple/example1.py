t = (10,20,(21,3.4,29),(22,3+4j),"python")
print(t)
print(type(t))
'''a=t[1][2] #  Type errror
print(a,type(a)) 
'''
a=t[2][1]
print(a)
b = t[2][2]
print(b)
print(t[2])
print(t[3][1])
'''t.append(8) # AttributeError := tupel object has no atribute 'append'
print(t)'''
a=t[2].count(21)
print(a)
b = t[2].index(21)
print(b)
c = t[2].index(3.4)
print(c)