a={1,2,3,4,1}
print(type(a))
print(a)
# important: This syntex will create an empty dictionary and not an empaty set
a={}
print(type(a))
#an Empty set can be created using the below syntex:
b=set()
print(type(b))
# mathod of Set 
b=set()
b.add(4)
b.add(5)
b.add((4,5,6))
print(b)
print(len(b))#print the lenth of this set
b.remove(4)
print(b)