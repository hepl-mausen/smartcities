#File : Button
#Turning on/off a led with a button 
#loic.mausen@student.hepl.be

import machine
button = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(18, machine.Pin.OUT)

while True:
    val = button.value()
    if val == 1:
        led.value(1)
    else:
        led.value(0)
        
        
import machine
import utime

button = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(18, machine.Pin.OUT)

val = 0

while True:
    if button.value() == 1:
        val = val + 1
        utime.sleep_ms(500)
        
    elif val == 2:
        val = 0
         
    led.value(val)
    
    

    