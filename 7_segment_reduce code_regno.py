'''write a micropython scrit to interface a common anode 7-segment display with esp32 
To display number 8 along with DP Pin 
note: terminal a-32,b-33,c-25,d-26,e-27,f-12,g-14,dp-13,
to display the Roll number with seven segment display infinite time 
'''
from machine import Pin
from time import sleep

Pins=[Pin(32,Pin.OUT), #a   initializing output pins
    Pin(33,Pin.OUT),  #b
    Pin(25,Pin.OUT),  #c
    Pin(26,Pin.OUT),  #d
    Pin(27,Pin.OUT),  #e
    Pin(12,Pin.OUT),   #f
    Pin(15,Pin.OUT),   #g
    Pin(13,Pin.OUT)]  #dp

digits=[[0,0,1,1,0,0,0,1],#p without dp
        [1,0,0,1,1,1,1,0],#1 with dp
        [0,0,1,0,0,1,0,1],# 2 without dp
        [0,1,0,0,1,0,0,0],#5 with dp
        [1,0,0,1,1,1,1,0],# 1 witout dp
        [0,1,0,0,0,0,0,0],# 6 with dp
        [0,0,0,0,0,0,1,1],# 0 without dp
        [1,0,0,1,1,0,0,0],# 4 with dp
        [0,0,0,0,0,0,0,1],# 8 without dp
        ]
while True:
    for i in range(9):
        for j in range(8):
            Pins[j].value(digits[i][j])
        sleep(1)