t = 1,22,44,"sangha",33+4j,1,22,44,"sangha",33+4j,22,1,44
print(t,type(t),len(t),id(t))
a = t.count(22) #This Function is used for Finding the Number of Occurences (Frequency) of Value from tuple Object.
print(a,type(a),id(a))
b = t.count("sangha")
print(f"no of occurence of 22 in t ={b} ,{type(b)},{id(b)}")
c = t.count(44)
print(c,type(c),id(c))


print("="*80)
for value in t:
    print(f"{value}==>{type(value)}==>{type(t)}")