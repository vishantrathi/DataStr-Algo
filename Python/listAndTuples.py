#list and tuples in python


row=[1,2,3,4,5]
row.append('6')
row.append('7')# add element at the end of the list
print(row)
row.insert(0,'kia') #insert at an index
print(row)
print(row.index('kia')) # if several present it will return the first index of the element

row.remove('kia') # remove the first occurrence of the element
print(row)  
row.pop(5)
print(row) # remove the last element of the list


#multidimestional list
# 2d list of list
lot_2d=[['toyota','honda'],
        ['bmw','audi'],
        ['mercedes','volkswagen']]
#3d list of list of list
lot_3d=[[['tesla','ford']],# first floor
        [['sabaru','nissan']],#second floow
        [['volkswagen','new motor']]]#third floor


print(lot_2d)
print(lot_2d[0][0]) #can access the car at 0 0
print(lot_2d[1])
print(lot_2d[2])

print(lot_3d[0][0][0])
print(lot_3d[1])
print(lot_3d[2])

for floor in lot_3d:
    for raw in floor:
        for car in raw:
            print(car)