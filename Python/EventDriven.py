#Event-Driven Programming is a programming paradigm in which the flow of the program is controlled by events. The program waits for an event (such as a button click, key press, mouse click, timer, or network message) and executes a specific function (called an event handler or callback) when that event occurs

# 1 event at a time can handle by event driven program

import asyncio
import time

def alarm(): #handle for when the alarm goes off 
    print('Wake up!')
    print('Calling the pizza Company.\n')
    loop.call_later(1,alarm) # schedule another alarm

def doorbell():  #handle for when doorbell rings
    print('Dind Ding')
    print('Thanks for bringing pizza....')

def phoneCall(): #handle for when phone rings
    print('Ring Ring')
    print('Answering the phone..... Hello who is this/n')

loop=asyncio.get_event_loop()
loop.call_later(1,alarm)  #schedule initial alarm event
loop.call_later(4,doorbell) #schedule doorbell event
loop.call_later(5,phoneCall) #schdule phone call event

print('starting the event loop.../n')
loop.run_forever() # the code below this never executed because loop runs forever

print('The event loop stopped; closing it down')
loop.close()