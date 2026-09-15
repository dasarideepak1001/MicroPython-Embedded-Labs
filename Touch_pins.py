'''
micro-python script with touch GPIO ports every half second 
and print the touch value results in shell window read and infinite time touchpin values

'''
from machine import Pin, TouchPad
from time import sleep as s

LED0=Pin(2,Pin.OUT)

threshold=200

while True:
    touch_Pin4=TouchPad(Pin(4, mode=Pin.IN))
    touch_value=touch_Pin4.read()
    print("Touch Value: ", touch_value)
    if (touch_value<200):
        LED0.on()
        print("Touch")
    else:
        LED0.off()
        print("No Touch")