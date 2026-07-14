setOne={1,2,3,4,5,6,7,8}
setTwo={1,3,4,6,8,9}

setthree=setOne.intersection(setTwo) #Returns the elements that are present in both sets.
print(setthree)
setFour=setOne.difference(setTwo) #Returns the elements that are in the first set but not in the second.
print(setFour)
setfive=setOne.symmetric_difference(setTwo) # Returns elements that are in either set, but not in both.
print(setfive)

print(8 in setOne)
setOne.pop()
print(setOne)
setOne.add(11)
print(setOne)
setOne.remove(11)
print(setOne)

