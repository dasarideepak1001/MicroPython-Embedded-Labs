'''
Micropython script to toggle an LED for n-number of times
Toggling rate to be 1 second LED is connected to Pin-2 of ESP32
only for nad while also
'''

from machine import Pin  #to import pin class machine module 
from time import sleep  as sec # to import sleep function from time module and create a object
 
LED0=Pin(2,Pin.OUT)    #created an object (led1) for Pin(2,Pin.OUT)
'''
while 1:              #infinite loop by while loop 
    LED0.on()        #calling on function from pin class with respect to time
    sec(2)           #stop for 2 sec
    LED0.off()       #calling off function from pin class with respect to time
    sec(2)          #stop for 2 sec

while 1:             #infinite loop
    LED0.value(1)    #calling on function by value from pin class w.r.t time
    sec(2)           #  stop for 2 secs
    LED0.value(0)    #calling off function by value from pin class w.r.t time
    sec(2)           # stop for 2 secs
'''
x=LED0.value()
print(x)

for i in range(10):
    print("i= ", i)
    LED0.value(1)
    sec(1)
    LED0.value(0)
    sec(1)



'''
n=0
while n<10:
    LED0.value(not LED0.value()) #led0.value(true)
    sec(1)
    n=n+1

print("END")'''