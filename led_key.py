'''micropython script to control and LED with respect to the position of a KEY
LED is connect to Pin-2 of ESP32
KEY is connect to Pin-4 of ESP32
note: LED should be off upon
turning ON the KEY , viceversa'''

from machine import Pin # Initialize LED pin (GPIO 2) as an output device

LEDr = Pin(2, Pin.OUT)  # Initialize KEY pin (GPIO 4) as an input device
KEY = Pin(4, Pin.IN)   # Continuously monitor the switch state and update the LED inverse-proportionally

while True:      # Read the current digital value of the KEY (0 or 1)
    KEY_status = KEY.value()    # If the KEY reads HIGH (1), turn the LED OFF (0)

    if(KEY_status == 1):    # If the KEY reads LOW (0), turn the LED ON (1)
        LEDr.value(0)
    else:
        LEDr.value(1)
