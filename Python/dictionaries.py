# Dictionaries use hash fn to retrive the store data
# Dictionaries store data as key-value pairs
# Dictionaries use a hash table to store key-value pairs.
# Keys are hashed, allowing fast lookup, insertion, and deletion.
dist={'Aron':1,
      'Dom':2,
      'richa':3,
      'jad':4}

print(dist)
print(dist['Aron'])
print(hash('Aron'))

dist['John'] = 5 #Add Into Dictionsries
print(dist)

dist['Aron']=1212 #overwritten the value
print(dist)

#can have dublicate values
#can store diff type of object as the value'

dist['Aron']=(1212,3456)
print(dist)


def caller_id(lookup_number):
    for name, numbers in dist.items():
        if isinstance(numbers, tuple):
            if lookup_number in numbers:
                return name



print(caller_id(3))
print(caller_id(1212))


#order of key value pair is on their insertion order