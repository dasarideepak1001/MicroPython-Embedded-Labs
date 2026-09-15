from machine import Pin
import time 

# Initialize 7-segment pins as Output Pins
A = Pin(32, Pin.OUT)
B = Pin(33, Pin.OUT)
C = Pin(25, Pin.OUT)
D = Pin(26, Pin.OUT)
E = Pin(27, Pin.OUT)
F = Pin(12, Pin.OUT)
G = Pin(15, Pin.OUT)
DP = Pin(13, Pin.OUT)

# Display '1' with DP ON
def display_one():
    A.value(1)
    B.value(0)
    C.value(0)
    D.value(1)
    E.value(1)
    F.value(1)
    G.value(1)
    DP.value(0)  # DP ON

# Display '2' with DP OFF
def display_two():
    A.value(0)
    B.value(0)
    C.value(1)
    D.value(0)
    E.value(0)
    F.value(1)
    G.value(0)
    DP.value(1)  # DP OFF

# Display '5' with DP ON
def display_five():
    A.value(0)
    B.value(1)
    C.value(0)
    D.value(0)
    E.value(1)
    F.value(0)
    G.value(0)
    DP.value(0)  # DP ON

# Display '6' with DP OFF
def display_six():
    A.value(0)
    B.value(1)
    C.value(0)
    D.value(0)
    E.value(0)
    F.value(0)
    G.value(0)
    DP.value(1)  # DP OFF

# Display '0' with DP ON
def display_zero():
    A.value(0)
    B.value(0)
    C.value(0)
    D.value(0)
    E.value(0)
    F.value(0)
    G.value(1)
    DP.value(0)  # DP ON

# Display '4' with DP OFF
def display_four():
    A.value(1)
    B.value(0)
    C.value(0)
    D.value(1)
    E.value(1)
    F.value(0)
    G.value(0)
    DP.value(1)  # DP OFF

# Display '8' with DP ON
def display_eight():
    A.value(0)
    B.value(0)
    C.value(0)
    D.value(0)
    E.value(0)
    F.value(0)
    G.value(0)
    DP.value(0)  # DP ON

# Infinite loop cycling through roll number sequence
while True:
    display_one()
    time.sleep(1)
    
    display_two()
    time.sleep(1)
    
    display_five()
    time.sleep(1)
    
    display_six()
    time.sleep(1)
    
    display_zero()
    time.sleep(1)
    
    display_four()
    time.sleep(1)
    
    display_eight()
    time.sleep(1)