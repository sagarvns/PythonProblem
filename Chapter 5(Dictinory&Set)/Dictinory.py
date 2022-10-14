myDict ={
    "Fast":"In a Quick Manner",
    "Sagar":"Coad",
    "mark":[1,2,3,4],
    "anotherdict":{'harry':'player'}
}
print(myDict['Fast'])
print(myDict['Sagar'])
myDict['mark']=[12,14]
print(myDict['mark'])

print(myDict['anotherdict']['harry'])

#mathod of Dictonery
myDict ={
    "fast":"In a Quick Manner",
    "sagar":"Coad",
    "mark":[1,2,3,4],
    "anotherdict":{'harry':'player'},
    1:2
}
print(type(myDict.keys()))#type of keys()
print(list(myDict.keys()))# all key 
print(list(myDict.values()))# all values 
print(list(myDict.items()))# all the(key,value)for all items of the dictionary 
print(myDict)

updateDict={
    "loveish":"friend",
    "sagar":"BCA"
}
myDict.update(updateDict)
print(myDict)

