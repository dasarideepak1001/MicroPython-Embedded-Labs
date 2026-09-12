'''Micro-python script to control an LED w.r.t position of a
 switch led is connected to pin 2 switch is connected to pin 4
note:use internal pul down resistor if the switch led to be ON or viceversa
'''
from machine import Pin  #to import pin class machine module 
import time

led = Pin(2, Pin.OUT)   # Initialize LED on pin 2 as an output
switch = Pin(4, Pin.IN, Pin.PULL_DOWN)  # Initialize switch on pin 4 as an input with an internal pull-down resistor

while True:
 
  if switch.value() == 1:     # When the switch is pushed, pin 4 reads HIGH (1), turning the LED ON
    led.on()
  else:
    led.off()

  time.sleep(0.05)