tup = (10,"pyhton",[1,2,3],[6,4,9],"Guido")
print(tup,type(tup))

print("="*40)
for val in tup:
    print(f"{val}==> {type(val)}==>{type(tup)}")
print("="*40)


a = tup[2]
print(a,type(a))
tup[2].append(89)
print(tup)