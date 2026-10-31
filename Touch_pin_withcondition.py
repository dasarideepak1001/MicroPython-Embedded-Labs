'''
micro-python script with touch GPIO ports every half second 
and print the touch value results in shell window read and infinite time 
touchpin values
not:a toggle (or latching) behavior: when touch the pin once to turn the LED on, 
it stays on even after take your finger away, and it stays on until  
touch the pin a second time (when the threshold goes low again) to turn it off
'''
from machine import Pin, TouchPad
from time import sleep as s

LED0 = Pin(2, Pin.OUT)
threshold = 200

led_status = False
touch_previously = False

while True:
    touch_Pin4 = TouchPad(Pin(4, mode=Pin.IN))
    touch_value = touch_Pin4.read()
    print("Touch Value: ", touch_value)
    if (touch_value<200):
        print("Touch")
        if not touch_previously:
            led_status = not led_status 
            if led_status:
                LED0.on()
                print("LED Turned ON")
            else:
                LED0.off()
                print("LED Turned OFF")
        touch_previously = True
    else:
        print("No Touch")
        touch_previously = False
        
    s(0.5)