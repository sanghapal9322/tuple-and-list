lst =[1,2,3,(20,30,40),(10,50,60),"python"]
print(lst,type(lst))

print("="*40)

for val in lst:
    print(f"{val}==>{type(val)}==>type(lst)")

print("="*40)

lst.insert(-1,800)
print(lst)

a=lst[3]
print(a)
b=tuple(sorted(lst[4],reverse=True))
print(b)
c = tuple(sorted(lst[3],reverse=True))
print(c)