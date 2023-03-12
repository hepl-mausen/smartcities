#File : Blinking led 
#making led blink with for and while loops 
#loic.mausen@student.hepl.be

### for loop ###

import machine
import utime
LED = machine.Pin(16,machine.Pin.OUT)

for i in range (10):
    LED.value(1)
    utime.sleep_ms(1000)
    LED.value(0)
    utime.sleep_ms(1000)
    
    
### while loop ###
    
import machine
import utime
LED = machine.Pin(16,machine.Pin.OUT)

while True :
    LED.value(1)
    utime.sleep_ms(1000)
    LED.value(0)
    utime.sleep_ms(1000)