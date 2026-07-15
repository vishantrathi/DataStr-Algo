#Polling is a technique where a program repeatedly checks whether something has happened or whether new data is available.

hungry = True

while(hungry):
    print('open the door')
    front_door = open("front_door.txt", "r", encoding="utf-8")
    content = front_door.read()
    if "Delivery person" in content:
        print("The pizza is here!!!!!!!")
        hungry = False
    else:
        print("Not yet")
    
    print('closing the front door')
    front_door.close()