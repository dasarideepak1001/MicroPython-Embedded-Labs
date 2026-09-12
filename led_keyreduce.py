'''micropython script to control and LED with respect to the position of a KEY
LED is connect to Pin-2 of ESP32
KEY is connect to Pin-4 of ESP32
note: LED should be off upon
turning ON the KEY , viceversa'''

from machine import Pin   # Initialize the LED pin as an output and the KEY pin as an input on a single line

LEDr = Pin(2, Pin.OUT)
KEY = Pin(4, Pin.IN)  
  # Continuously read the key state and assign its logical inverse directly to the LED

while True:
    LEDr.value(not KEY.value())